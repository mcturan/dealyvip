import re

with open('src/pages/en/guides/[slug].astro', 'r') as f:
    content = f.read()

# Add related guides logic
pattern1 = r'const tools = relatedToolIds\.length > 0 \n  \? allTools\.filter\(tool => relatedToolIds\.includes\(tool\.id\)\)\n  : \[\];'
replacement1 = """const tools = relatedToolIds.length > 0 
  ? allTools.filter(tool => relatedToolIds.includes(tool.id))
  : [];

const allGuides = await getCollection('guides', ({ id }) => id.startsWith('en/'));
const relatedGuideIds = guide.data.relatedGuides || [];
const relatedGuides = relatedGuideIds.length > 0
  ? allGuides.filter(g => relatedGuideIds.includes(g.id.replace('en/', '').replace(/\.md$/, '')))
  : [];"""

content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)

pattern2 = r'\{tools\.length > 0 && \('
replacement2 = """{relatedGuides.length > 0 && (
        <div style="margin-top: var(--space-xl); padding-top: var(--space-lg); border-top: 1px solid var(--color-border);">
          <h2 style="font-size: 1.5rem; margin-bottom: var(--space-md);">Related Guides</h2>
          <div class="grid" style="grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: var(--space-md);">
            {relatedGuides.map(relGuide => (
              <a href={`/en/guides/${relGuide.id.replace('en/', '').replace(/\.md$/, '')}/`} class="card no-underline" style="display: block; transition: border-color 0.2s;">
                <h3 style="font-size: 1.1rem; margin: 0 0 0.5rem 0; color: var(--color-primary);">{relGuide.data.title}</h3>
                <p class="text-muted" style="font-size: 0.85rem; margin: 0;">{relGuide.data.description}</p>
              </a>
            ))}
          </div>
        </div>
      )}
      
      {tools.length > 0 && ("""

content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)

with open('src/pages/en/guides/[slug].astro', 'w') as f:
    f.write(content)
