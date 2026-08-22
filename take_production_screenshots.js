import { chromium } from 'playwright';
import fs from 'fs';

// We test against Nginx which we configured to run on 8081
const port = 8081;

if (!fs.existsSync('screenshots')) {
  fs.mkdirSync('screenshots');
}

(async () => {
  const browser = await chromium.launch();
  
  const viewports = [
    { width: 375, height: 667, name: 'mobile' },
    { width: 1280, height: 800, name: 'desktop' }
  ];

  const routes = [
    { path: '/en/', name: 'prod-home' },
    { path: '/en/assistance/', name: 'prod-assistance' },
    { path: '/en/contact/', name: 'prod-contact' },
    { path: '/en/tools/turkiye/', name: 'prod-turkiye' }
  ];
  
  for (const route of routes) {
    console.log(`Taking production screenshots for: ${route.path}`);
    const context = await browser.newContext();
    const page = await context.newPage();
    
    await page.goto(`http://127.0.0.1:${port}${route.path}`, { waitUntil: 'networkidle' });
    
    for (const vp of viewports) {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      await page.waitForTimeout(500);
      
      await page.screenshot({ 
        path: `screenshots/${route.name}-${vp.name}-full.png`, 
        fullPage: true 
      });
    }
    
    await context.close();
  }
  
  await browser.close();
  console.log("Production screenshots captured successfully.");
  process.exit(0);
})();
