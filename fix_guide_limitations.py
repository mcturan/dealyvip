with open('src/pages/en/guides/[slug].astro', 'r') as f:
    content = f.read()

content = content.replace(
    "import ContactCTA from '../../../components/ContactCTA.astro';",
    "import ContactCTA from '../../../components/ContactCTA.astro';\nimport VerificationLimitations from '../../../components/VerificationLimitations.astro';"
)

tools_block = """{tools.length > 0 && (
        <div style="margin-top: var(--space-xl); padding-top: var(--space-lg); border-top: 1px solid var(--color-border);">
          <h2 style="font-size: 1.5rem; margin-bottom: var(--space-md);">Related Verification Tools</h2>
          <VerificationLimitations context="guides" />
          <div class="grid" style="grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: var(--space-md);">"""

content = content.replace(
    """{tools.length > 0 && (
        <div style="margin-top: var(--space-xl); padding-top: var(--space-lg); border-top: 1px solid var(--color-border);">
          <h2 style="font-size: 1.5rem; margin-bottom: var(--space-md);">Related Verification Tools</h2>
          <div class="grid" style="grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: var(--space-md);">""",
    tools_block
)

with open('src/pages/en/guides/[slug].astro', 'w') as f:
    f.write(content)

