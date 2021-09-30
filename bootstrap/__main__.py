import argparse
from typing import List, Tuple
import sc
import os

from bootstrap.step import Step
from termcolor import colored

import jinja2

current_dir = os.path.dirname(os.path.abspath(__file__))

def collect_steps(dir_path: str) -> List[Tuple[str, str]]:
  collected = []
  for root, _, files in os.walk(dir_path, topdown=False):
    for name in files:
      if root == dir_path:
        collected.append((name, os.path.join(root, name)))

  return collected

def run(args):
  memory = sc.Memory(args.config)
  driver = memory.client.driver

  dir_path = os.path.join(current_dir, "steps")
  print("Collecting steps ... ", end='')
  steps = collect_steps(dir_path)
  print(colored(f"{len(steps)}", "white"))
  
  sorted_steps = sorted(steps, key=lambda x: x[0])

  env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(dir_path),
    autoescape=jinja2.select_autoescape())

  total_time = 0

  passed = True
  for name, file_name in sorted_steps:
    step = Step(driver, env.get_template(name), memory.config)

    print("Run " + colored(name, "blue") + " ... ", end='')
    res = step.run()
    if res:
      t = (res.result_available_after + res.result_consumed_after) / 1000.0
      total_time += t
      print(colored("✓", "green") + f" - {t:.3f} s" if res else colored("✕", "red"))
    elif res is None:
      passed = False
      print("Errors:")
      for err in step.errors:
        print (f'  - {err}')

      break

  if passed:
    print("Complete " + colored("successfully", "green") + f" in {total_time:.3f} seconds")
  else:
    print(colored("Failed", "red"))

  return passed

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Initialize database with core elements')
  parser.add_argument("--config", type=str, required=True, help="Path to config file")
  args = parser.parse_args()

  run(args)