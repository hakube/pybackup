import argparse
from pybackup.backup import Backup
import sys

args = argparse.ArgumentParser(prog="pybackup")
args.add_argument('--config', required=True, help='Path to config file')
args.add_argument('--echo','-e', action='store_true', help="Prints out the config file")
args = args.parse_args()

def main():
    backup = Backup(args.config)
    backup.parse_yaml()

    if args.echo:
        sys.exit(backup.echo())
    