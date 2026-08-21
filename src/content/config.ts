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
    isDraft: z.boolean().default(false),
  }),
});

export const collections = {
  'guides': guidesCollection,
};
