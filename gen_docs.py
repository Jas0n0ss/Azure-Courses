import os

ROOT = '.'
INDEX_MD = 'index.md'

def get_subprojects(root):
    return [
        name for name in os.listdir(root)
        if os.path.isdir(name) and not name.startswith('.') and name != '__pycache__'
    ]

def ensure_readme(subproject):
    readme_path = os.path.join(subproject, 'README.md')
    if not os.path.exists(readme_path):
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(f'# {subproject}\n\n')
            f.write(f'本项目 `{subproject}` 的详细内容。\n\n')
            # 自动列出子项目下的 Markdown 文件
            md_files = [
                fn for fn in os.listdir(subproject)
                if fn.endswith('.md') and fn != 'README.md'
            ]
            if md_files:
                f.write('## 目录\n')
                for md in sorted(md_files):
                    f.write(f'- [{md}](./{md})\n')
                f.write('\n')

def generate_index_md(subprojects):
    with open(INDEX_MD, 'w', encoding='utf-8') as f:
        f.write('# Azure Courses 目录\n\n')
        f.write('欢迎阅读本项目，每个子项目均可单独阅读：\n\n')
        for name in sorted(subprojects):
            if os.path.exists(os.path.join(name, 'README.md')):
                f.write(f'- [{name}](./{name}/README.md)\n')

if __name__ == '__main__':
    subs = get_subprojects(ROOT)
    for sub in subs:
        ensure_readme(sub)
    generate_index_md(subs)
    print('文档结构已自动生成！')