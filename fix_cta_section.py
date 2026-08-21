import re

with open('src/components/CTASection.astro', 'r') as f:
    content = f.read()

content = content.replace('btnText = "Contact DealyVIP"', 'btnText = "Explore Coordination Options"')

with open('src/components/CTASection.astro', 'w') as f:
    f.write(content)
