import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  
  const urls = [
    'http://localhost:8081/en/',
    'http://localhost:8081/en/guides/verify-turkish-company/'
  ];
  
  for (const url of urls) {
    await page.goto(url);
    try {
      const results = await new AxeBuilder({ page }).analyze();
      console.log(`\nAccessibility Results for: ${url}`);
      console.log(`Violations: ${results.violations.length}`);
      
      if (results.violations.length > 0) {
        results.violations.forEach((v, i) => {
          console.log(`\n${i+1}. [${v.impact}] ${v.id}: ${v.help}`);
          console.log(`   Description: ${v.description}`);
          v.nodes.forEach(node => {
            console.log(`   - Target: ${node.target.join(', ')}`);
          });
        });
      }
    } catch (e) {
      console.error('Error running accessibility test:', e);
    }
  }
  
  await browser.close();
  process.exit(0);
})();
