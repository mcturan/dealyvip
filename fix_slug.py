import re

with open('src/pages/en/guides/[slug].astro', 'r') as f:
    content = f.read()

# Replace the tools definition block
pattern = r'let tools = \[\];\s*if \(guide\.data\.relatedTools && guide\.data\.relatedTools\.length > 0\) \{\s*const allTools = await getCollection\(\'tools\'\);\s*tools = allTools\.filter\(tool => guide\.data\.relatedTools\.includes\(tool\.id\)\);\s*\}'

replacement = """const allTools = await getCollection('tools');
const relatedToolIds = guide.data.relatedTools || [];
const tools = relatedToolIds.length > 0 
  ? allTools.filter(tool => relatedToolIds.includes(tool.id))
  : [];"""

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('src/pages/en/guides/[slug].astro', 'w') as f:
    f.write(new_content)
