import re

with open('src/pages/en/tools/[country].astro', 'r') as f:
    content = f.read()

# Add getAccessTypeColor
helpers = """const formatCategory = (cat: string) => {
  return cat.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
};

const getStatusColor = (status: string) => {
  switch(status) {
    case 'OFFICIAL': return 'background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd;';
    case 'INSTITUTIONAL': return 'background: #fef9c3; color: #a16207; border: 1px solid #fde047;';
    case 'THIRD-PARTY': return 'background: #f3f4f6; color: #4b5563; border: 1px solid #e5e7eb;';
    case 'INFORMATIONAL': return 'background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0;';
    default: return 'background: #eee; color: #333;';
  }
};

const formatAccessType = (type: string) => {
  return type.replace(/_/g, ' ');
};

const getAccessTypeColor = (type: string) => {
  switch(type) {
    case 'PUBLIC': return 'color: #15803d;';
    case 'PUBLIC_WITH_LIMITATIONS': return 'color: #b45309;';
    case 'REGISTRATION_REQUIRED': return 'color: #0369a1;';
    case 'LOGIN_REQUIRED': return 'color: #6b21a8;';
    case 'EXTERNAL_PROFESSIONAL_REQUIRED': return 'color: #be123c;';
    case 'INFORMATION_ONLY': return 'color: #4b5563;';
    default: return 'color: #333;';
  }
};"""

content = re.sub(
    r"const formatCategory[\s\S]*?(?=\-\-\-)",
    helpers + "\n",
    content
)

# Replace the card content to include the new fields
card_new = """<div class="card" style="display: flex; flex-direction: column; gap: 1rem;">
                <div>
                  <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                    <h3 style="font-size: 1.25rem; margin: 0;">{tool.data.name}</h3>
                    <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.25rem;">
                      <span style={`font-size: 0.65rem; font-weight: 700; padding: 0.2rem 0.5rem; border-radius: 4px; ${getStatusColor(tool.data.officialStatus)}`}>
                        {tool.data.officialStatus}
                      </span>
                      <span style={`font-size: 0.65rem; font-weight: 700; ${getAccessTypeColor(tool.data.accessType)}`}>
                        {formatAccessType(tool.data.accessType)}
                      </span>
                    </div>
                  </div>
                  <p class="text-muted" style="font-size: 0.9rem; margin: 0;">Operated by: {tool.data.operator}</p>
                </div>
                
                <p style="font-size: 0.95rem; margin: 0;">{tool.data.shortDescription}</p>
                
                <div style="background: var(--color-slate-50); padding: 1rem; border-radius: 4px; font-size: 0.85rem;">
                  <strong style="color: #166534; display: block; margin-bottom: 0.25rem;">✓ Can Verify:</strong>
                  <ul style="margin: 0 0 0.75rem 1rem; padding: 0; color: #374151;">
                    {tool.data.whatItCanVerify.map(item => <li>{item}</li>)}
                  </ul>
                  
                  <strong style="color: #991b1b; display: block; margin-bottom: 0.25rem;">✗ Cannot Verify:</strong>
                  <ul style="margin: 0 0 0 1rem; padding: 0; color: #374151;">
                    {tool.data.whatItCannotVerify.map(item => <li>{item}</li>)}
                  </ul>
                  
                  {tool.data.requiredInformation && tool.data.requiredInformation.length > 0 && (
                    <>
                      <strong style="color: #0369a1; display: block; margin-bottom: 0.25rem; margin-top: 0.75rem;">ℹ️ Required Info:</strong>
                      <ul style="margin: 0 0 0 1rem; padding: 0; color: #374151;">
                        {tool.data.requiredInformation.map(item => <li>{item}</li>)}
                      </ul>
                    </>
                  )}
                </div>
                
                {tool.data.accessLimitations && (
                  <div style="font-size: 0.85rem; color: #854d0e; background: #fefce8; padding: 0.75rem; border-left: 3px solid #eab308;">
                    <strong>Access Note:</strong> {tool.data.accessLimitations}
                  </div>
                )}
                
                <div style="margin-top: auto; padding-top: 1rem; border-top: 1px solid var(--color-border); display: flex; justify-content: space-between; align-items: center;">
                  <a href={tool.data.url} target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="padding: 0.4rem 0.8rem; font-size: 0.85rem;">Visit Resource &nearr;</a>
                  <div style="text-align: right;">
                    <span class="text-muted" style="display: block; font-size: 0.7rem; font-weight: 500;">LANG: {(tool.data.languages || []).join(', ').toUpperCase()}</span>
                  </div>
                </div>
              </div>"""

content = re.sub(
    r'<div class="card" style="display: flex; flex-direction: column; gap: 1rem;">.*?</div>(?=\n\s*</div)',
    card_new,
    content,
    flags=re.DOTALL
)

with open('src/pages/en/tools/[country].astro', 'w') as f:
    f.write(content)

