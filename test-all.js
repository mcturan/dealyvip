import { chromium, devices } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import { exec } from 'child_process';

const port = 9005;

// Start server
const server = exec(`http-server dist -p ${port}`);

setTimeout(async () => {
  const browser = await chromium.launch();
  
  const viewports = [
    { width: 320, height: 568, name: 'Mobile S' },
    { width: 375, height: 667, name: 'Mobile M' },
    { width: 768, height: 1024, name: 'Tablet' },
    { width: 1440, height: 900, name: 'Desktop' }
  ];

  const urls = [
    `http://127.0.0.1:${port}/en/`,
    `http://127.0.0.1:${port}/en/guides/verify-turkish-company/`
  ];
  
  for (const url of urls) {
    console.log(`\nTesting URL: ${url}`);
    
    // Accessibility
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto(url);
    const results = await new AxeBuilder({ page }).analyze();
    console.log(`A11y Violations: ${results.violations.length}`);
    if (results.violations.length > 0) {
      results.violations.forEach(v => {
        console.log(`- [${v.impact}] ${v.id}: ${v.description}`);
      });
    }
    
    // Responsive
    for (const vp of viewports) {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      const overflow = await page.evaluate(() => {
        return document.documentElement.scrollWidth > window.innerWidth;
      });
      console.log(`Viewport ${vp.name} (${vp.width}px): Horizontal overflow? ${overflow}`);
    }
    
    await context.close();
  }
  
  await browser.close();
  server.kill();
  process.exit(0);
}, 3000);
