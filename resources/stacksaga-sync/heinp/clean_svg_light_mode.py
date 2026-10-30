import os
import glob
import re

def replace_light_dark(text):
    while "light-dark(" in text:
        start = text.find("light-dark(")
        depth = 0
        comma_idx = -1
        end = -1
        for i in range(start + len("light-dark("), len(text)):
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                if depth == 0:
                    end = i
                    break
                else:
                    depth -= 1
            elif text[i] == ',' and depth == 0:
                comma_idx = i
        if end != -1 and comma_idx != -1:
            light_val = text[start + len("light-dark("):comma_idx].strip()
            text = text[:start] + light_val + text[end + 1:]
        else:
            break
    return text

def clean_svg(svg_path):
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace light-dark(...) with the light value
    content = replace_light_dark(content)

    # 2. Force light color-scheme
    content = re.sub(r'color-scheme:\s*light dark;', 'color-scheme: light;', content)

    # 3. Ensure solid white background on root <svg>
    content = re.sub(r'background:\s*transparent;\s*background-color:\s*transparent;', 'background: #ffffff; background-color: #ffffff;', content)

    # 4. Insert white background rect if not present
    if '<rect width="100%" height="100%" fill="#ffffff"/>' not in content:
        content = content.replace('<defs/>', '<defs/><rect width="100%" height="100%" fill="#ffffff"/>')

    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned {os.path.basename(svg_path)} -> Pure Light Mode with White Background")

if __name__ == '__main__':
    svg_dir = r"C:\Users\mafei\STACKSAGA-PROJECT\stacksaga-docs\docs\modules\implementations\images\stacksaga-sync\heinp"
    for svg_file in glob.glob(os.path.join(svg_dir, "*.svg")):
        clean_svg(svg_file)
