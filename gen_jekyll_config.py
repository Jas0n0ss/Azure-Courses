import os

PROJECT_TITLE = "Azure Courses"
DESCRIPTION = "A collection of Azure learning projects and labs."
GITHUB_URL = "https://your-github-username.github.io/Azure-Courses"  # 替换为你的GitHub Pages地址

def get_subprojects(root='.'):
    return [
        name for name in os.listdir(root)
        if os.path.isdir(name) and not name.startswith('.') and name != '__pycache__'
    ]

def gen_config_yaml(subprojects):
    lines = [
        '# Site settings',
        f'title: "{PROJECT_TITLE}"',
        f'description: "{DESCRIPTION}"',
        'baseurl: ""',
        f'url: "{GITHUB_URL}"',
        '',
        '# GitHub Pages and theme setup',
        'remote_theme: pages-themes/hacker@v0.2.0',
        'markdown: kramdown',
        '',
        '# Navigation and other configurations',
        'navbar:',
        '  - text: "首页"',
        '    url: "/README.md"',
    ]
    for sub in sorted(subprojects):
        lines.append(f'  - text: "{sub}"')
        lines.append(f'    url: "/{sub}/"')
    lines += [
        '',
        '# Author settings',
        'author:',
        '  bio: "Azure 学习者与实践者。"',
        '',
        '# Pagination settings (optional)',
        'paginate: 5',
        '',
        '# Exclude specific files or directories from being processed',
        'exclude:',
        '  - gen_docs.py',
        '  - gen_jekyll_config.py',
        '',
        '# Jekyll plugins (optional)',
        'plugins:',
        '  - jekyll-feed',
        '  - jekyll-seo-tag',
        '',
        'defaults:',
        '  - scope:',
        '      path: ""',
        '    values:',
        '      layout: "default"',
        '      author: "Your Name"',
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    subs = get_subprojects()
    config_content = gen_config_yaml(subs)
    with open('_config.yml', 'w', encoding='utf-8') as f:
        f.write(config_content)
    print('已自动生成 _config.yml，navbar 已包含所有子项目！')