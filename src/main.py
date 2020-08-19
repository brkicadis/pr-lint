import sys
import re
from termcolor import colored, cprint


def validate_pr_branch_name():
    branch_name = sys.argv[1]
    regex = sys.argv[2]
    print("Regex" + regex)
    if re.search(r"^(RC-(([0-9])+\.){2}([0-9])+-(patch|minor|major))$|-(test|documentation|feature|configuration|force)$|^(dependabot)", branch_name):
        cprint(colored("Branch name {} is valid".
                       format(branch_name)), 'green', attrs=['bold'], file=sys.stderr)
    else:
        cprint(colored("Branch name {} is invalid. Here are some accepted PR branch name examples:\n - TPWDCEE-XXX-test\n - RC-X.X.X-patch\n".
                       format(branch_name)), 'red', attrs=['bold'], file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    validate_pr_branch_name()
