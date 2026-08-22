import re

with open("src/components/SiteFooter.astro", "r") as f:
    content = f.read()

# Replace the specific nav strings
content = content.replace(
    '<nav aria-label="Footer Link Group"', 
    '<nav aria-label="Footer Navigation"', 1
)

content = content.replace(
    '<nav aria-label="Footer Link Group"', 
    '<nav aria-label="Footer Legal Navigation"', 1
)

with open("src/components/SiteFooter.astro", "w") as f:
    f.write(content)
