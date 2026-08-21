import re

with open('src/pages/en/guides/[slug].astro', 'r') as f:
    content = f.read()

# Add import
import_pattern = r"import BaseLayout from '../../../layouts/BaseLayout.astro';"
import_replacement = "import BaseLayout from '../../../layouts/BaseLayout.astro';\nimport ContactCTA from '../../../components/ContactCTA.astro';"
content = re.sub(import_pattern, import_replacement, content)

# Figure out context based on guide topic
logic_pattern = r'const \{ Content \} = await guide\.render\(\);'
logic_replacement = """const { Content } = await guide.render();
const ctaContext = guide.data.topic === 'Verification & Trust' ? 'verification' : 
                   guide.data.topic === 'Local Assistance & Travel' ? 'assistance' : 'general';"""
content = re.sub(logic_pattern, logic_replacement, content)

# Inject CTA after content
cta_pattern = r'<div class="prose" style="line-height: 1\.7; font-size: 1\.05rem; color: var\(--color-text\);">\s*<Content />\s*</div>'
cta_replacement = """<div class="prose" style="line-height: 1.7; font-size: 1.05rem; color: var(--color-text);">
        <Content />
      </div>
      
      <ContactCTA context={ctaContext} />"""
content = re.sub(cta_pattern, cta_replacement, content)

with open('src/pages/en/guides/[slug].astro', 'w') as f:
    f.write(content)
