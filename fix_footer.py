import re

with open('src/components/SiteFooter.astro', 'r') as f:
    content = f.read()

pattern = r'<a href="/en/about/" class="no-underline text-muted">About Us</a>'
replacement = r'<a href="/en/what-we-do/" class="no-underline text-muted">What We Do</a>'

new_content = re.sub(pattern, replacement, content)

with open('src/components/SiteFooter.astro', 'w') as f:
    f.write(new_content)
