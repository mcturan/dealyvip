import re

with open('src/content/config.ts', 'r') as f:
    content = f.read()

replacement = """const toolsCollection = defineCollection({
  type: 'data',
  schema: z.object({
    countryId: z.string(),
    name: z.string(),
    shortDescription: z.string(),
    category: z.string(),
    operator: z.string(),
    officialStatus: z.enum(['OFFICIAL', 'INSTITUTIONAL', 'THIRD-PARTY', 'INFORMATIONAL']),
    accessType: z.enum([
      'PUBLIC', 
      'PUBLIC_WITH_LIMITATIONS', 
      'REGISTRATION_REQUIRED', 
      'LOGIN_REQUIRED', 
      'INFORMATION_ONLY', 
      'EXTERNAL_PROFESSIONAL_REQUIRED'
    ]).default('PUBLIC'),
    languages: z.array(z.string()).default(['tr']),
    url: z.string(),
    whatItCanVerify: z.array(z.string()),
    whatItCannotVerify: z.array(z.string()),
    requiredInformation: z.array(z.string()).optional(),
    accessLimitations: z.string().optional(),
    lastVerified: z.string(),
  }),
});"""

content = re.sub(r"const toolsCollection = defineCollection\(\{[\s\S]*?\}\);", replacement, content)

with open('src/content/config.ts', 'w') as f:
    f.write(content)
