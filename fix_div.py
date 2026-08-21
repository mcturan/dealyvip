with open('src/pages/en/tools/[country].astro', 'r') as f:
    content = f.read()

content = content.replace("</div>\n              </div>\n            ))}", "</div>\n            ))}")
with open('src/pages/en/tools/[country].astro', 'w') as f:
    f.write(content)
