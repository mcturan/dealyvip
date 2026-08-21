import re

with open('src/components/SiteHeader.astro', 'r') as f:
    content = f.read()

pattern = r'<a href={`/en/about/`} class="nav-link">About Us</a>'
replacement = r'<a href={`/en/what-we-do/`} class="nav-link">What We Do</a>'

new_content = re.sub(pattern, replacement, content)

with open('src/components/SiteHeader.astro', 'w') as f:
    f.write(new_content)
