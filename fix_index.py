import re

with open('src/pages/en/index.astro', 'r') as f:
    content = f.read()

# Replace the GuideCard block
pattern = r'<h2 class="section-title">Business Guides</h2>\s*<div class="grid grid-cols-3">.*?</div>'
replacement = """<h2 class="section-title">Business Guides</h2>
      <div class="grid grid-cols-3">
        <GuideCard 
          title="How to Verify a Turkish Company" 
          category="Verification & Trust" 
          url="/en/guides/verify-turkish-company/" 
        />
        <GuideCard 
          title="Supplier & Factory Verification in Türkiye" 
          category="Verification & Trust" 
          url="/en/guides/supplier-factory-verification-turkiye/" 
        />
        <GuideCard 
          title="How to Verify a Ukrainian Company" 
          category="Verification & Trust" 
          url="/en/guides/verify-ukrainian-company/" 
        />
      </div>"""

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('src/pages/en/index.astro', 'w') as f:
    f.write(new_content)
