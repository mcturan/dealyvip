import { z, defineCollection } from 'astro:content';

const guidesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    language: z.enum(['en', 'tr', 'uk', 'ru']).default('en'),
    country: z.string().optional(),
    region: z.string().optional(),
    category: z.string().optional(),
    topic: z.string().optional(),
    tags: z.array(z.string()).optional(),
    priority: z.number().default(0),
    related_lang_id: z.string().optional(),
    lastUpdated: z.date(),
    relatedGuides: z.array(z.string()).optional(),
    relatedTools: z.array(z.string()).optional(),
    status: z.enum(['draft', 'beta', 'reviewed']).default('draft'),
    sourceType: z.string().optional(),
    isDraft: z.boolean().default(false),
  }),
});

const countriesCollection = defineCollection({
  type: 'data',
  schema: z.object({
    id: z.string(),
    name: z.string(),
    description: z.string(),
  }),
});

const toolsCollection = defineCollection({
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
});

export const collections = {
  'guides': guidesCollection,
  'countries': countriesCollection,
  'tools': toolsCollection,
};
