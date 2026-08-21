import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  outDir: './dist',
  server: { port: 3000 },
});
