if [ -z "$1" ]
then
      echo "Please specify path to antlr tool. For example:\033[1;34m generate_antlr.sh antlr-4.9.2-complete.jar\033[0m"
else
      java -jar $1 -Dlanguage=Python3 -o sc/scs/antlr -no-listener -no-visitor -Xexact-output-dir sc/scs/scs.g4
fi