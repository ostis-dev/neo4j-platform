import argparse
from typing import List, Tuple
import sc
import os

from bootstrap.step import Step
from termcolor import colored

current_dir = os.path.dirname(os.path.abspath(__file__))

def collect_steps() -> List[Tuple[str, str]]:
  collected = []
  for root, _, files in os.walk(os.path.join(current_dir, "steps"), topdown=False):
   for name in files:
     collected.append((name, os.path.join(root, name)))

  return collected

def run(args):
  memory = sc.Memory(args.config)
  driver = memory.client.driver

  print("Collecting steps ... ", end='')
  steps = collect_steps()
  print(colored(f"{len(steps)}", "white"))
  
  sorted_steps = sorted(steps, key=lambda x: x[0])

  total_time = 0

  passed = True
  for name, file_name in sorted_steps:
    step = Step(driver, file_name, memory.config)

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