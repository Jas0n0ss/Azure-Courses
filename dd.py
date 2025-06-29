import os
import shutil

def remove_dir_if_exists(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"已删除: {path}")

def clean_all_subdirs(root='.'):
    for name in os.listdir(root):
        subdir = os.path.join(root, name)
        if os.path.isdir(subdir):
            git_dir = os.path.join(subdir, '.git')
            github_dir = os.path.join(subdir, '.github')
            remove_dir_if_exists(git_dir)
            remove_dir_if_exists(github_dir)

if __name__ == '__main__':
    clean_all_subdirs()
    print("所有子目录下的 .git 和 .github 文件夹已清除。")