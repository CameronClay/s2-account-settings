import sys
import os
import shutil
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=dir_path, help="Path to StarCraft II Documents directory")
    incl = parser.add_argument_group('include (at least one of these flags is required)', 'files to symlink to all accounts')
    incl.add_argument("-k", "--hotkeys", action="store_true", help="Copy hotkeys from $dir/Hotkeys to all accounts")
    incl.add_argument("-v", "--variables", action="store_true", help="Copy variables from $dir/Account-Variables/Variables.txt to all accounts")
    args = parser.parse_args()

    if not (args.hotkeys or args.variables):
        parser.error('Must specify files/directories to symlink to all accounts (-k/-v)')
    
    path = os.path.normpath(args.dir)
    link_accounts(path, args.hotkeys, args.variables)

#returns true if removed
def remove_path(path : str, is_dir : bool = False) -> bool:
    if not (os.path.exists(path) or os.path.islink(path)): #if not valid file or directory or broken symlink
        return False
    
    removed = True
    if is_dir:
        if os.path.islink(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
        else:
            removed = False
    else:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.islink(path):
            os.unlink(path)
        else:
            removed = False

    return removed

def create_link(src_path : str, dst_path : str, is_dir : bool = False):
    removed = remove_path(dst_path, is_dir)
    
    if removed:
        print(f'Removed {dst_path}')

    os.symlink(src_path, dst_path, is_dir)
    print(f'Creating symlink {src_path}->{dst_path}')

def dir_path(path : str):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"dir_path:{path} is not a valid path")

def link_accounts(path : str, hotkeys : bool, variables : bool):
    subdirs = os.listdir(f'{path}/Accounts')
    for account in subdirs:
        if hotkeys:
            create_link(f'{path}/Hotkeys/', f'{path}/Accounts/{account}/Hotkeys', True)
        if variables:
            create_link(f'{path}/Account-Variables/Variables.txt', f'{path}/Accounts/{account}/Variables.txt', False)

if __name__ == '__main__':
    main()