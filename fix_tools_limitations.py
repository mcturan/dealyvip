with open('src/pages/en/tools/[country].astro', 'r') as f:
    content = f.read()

content = content.replace(
    "import BaseLayout from '../../../layouts/BaseLayout.astro';",
    "import BaseLayout from '../../../layouts/BaseLayout.astro';\nimport VerificationLimitations from '../../../components/VerificationLimitations.astro';"
)

content = content.replace(
    """<h1 class="display-title" style="margin-bottom: var(--space-sm);">{country.data.name} Verification Tools</h1>
    <p class="lead text-muted" style="max-width: 800px; margin-bottom: var(--space-xl);">
      {country.data.description} Please review the limitations of each tool carefully before relying on the data for financial decisions.
    </p>""",
    """<h1 class="display-title" style="margin-bottom: var(--space-sm);">{country.data.name} Verification Tools</h1>
    <p class="lead text-muted" style="max-width: 800px; margin-bottom: var(--space-xl);">
      {country.data.description} Please review the limitations of each tool carefully before relying on the data for financial decisions.
    </p>
    
    <VerificationLimitations />"""
)

with open('src/pages/en/tools/[country].astro', 'w') as f:
    f.write(content)
