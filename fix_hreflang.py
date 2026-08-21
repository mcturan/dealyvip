import re

with open('src/layouts/BaseLayout.astro', 'r') as f:
    layout = f.read()

layout = layout.replace(
    '<MetaHead title={title} description={description} />',
    '<MetaHead title={title} description={description} alternatives={alternatives} />'
)

with open('src/layouts/BaseLayout.astro', 'w') as f:
    f.write(layout)

meta_head = """---
interface AlternateLink {
  code: string;
  name: string;
  url: string;
}

interface Props {
  title: string;
  description: string;
  canonical?: string;
  alternatives?: AlternateLink[];
}

const { title, description, canonical, alternatives = [] } = Astro.props;
---
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} | DealyVIP</title>
<meta name="description" content={description} />
{canonical && <link rel="canonical" href={canonical} />}
<meta property="og:title" content={`${title} | DealyVIP`} />
<meta property="og:description" content={description} />
<meta property="og:type" content="website" />
{alternatives.map(alt => (
  <link rel="alternate" hreflang={alt.code} href={`https://dealyvip.com${alt.url}`} />
))}
"""
with open('src/components/MetaHead.astro', 'w') as f:
    f.write(meta_head)
