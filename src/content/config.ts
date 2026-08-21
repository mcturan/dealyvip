import { z, defineCollection } from 'astro:content';

const guidesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    language: z.enum(['en', 'tr', 'uk', 'ru']).default('en'),
    country: z.string().optional(),
    topic: z.string(),
    priority: z.number().default(0),
    related_lang_id: z.string().optional(),
    lastUpdated: z.date(),
    relatedTools: z.array(z.string()).optional(),
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
    url: z.string(),
    whatItCanVerify: z.array(z.string()),
    whatItCannotVerify: z.array(z.string()),
    accessLimitations: z.string().optional(),
    lastVerified: z.string(),
  }),
});

export const collections = {
  'guides': guidesCollection,
  'countries': countriesCollection,
  'tools': toolsCollection,
};
