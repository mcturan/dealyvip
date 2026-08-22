import { chromium } from 'playwright';
import { exec } from 'child_process';
import fs from 'fs';

const port = 9006;

// Create screenshots directory
if (!fs.existsSync('screenshots')) {
  fs.mkdirSync('screenshots');
}

// Start server
const server = exec(`npx http-server dist -p ${port}`);

setTimeout(async () => {
  const browser = await chromium.launch();
  
  const viewports = [
    { width: 375, height: 667, name: 'mobile' },
    { width: 1280, height: 800, name: 'desktop' }
  ];

  const routes = [
    { path: '/en/', name: 'home' },
    { path: '/en/assistance/', name: 'assistance' },
    { path: '/en/countries/', name: 'countries' },
    { path: '/en/what-we-do/', name: 'what-we-do' },
    { path: '/en/contact/', name: 'contact' }
  ];
  
  for (const route of routes) {
    console.log(`Taking screenshots for: ${route.path}`);
    const context = await browser.newContext();
    const page = await context.newPage();
    
    // We want to wait for network idle to ensure everything is loaded
    await page.goto(`http://127.0.0.1:${port}${route.path}`, { waitUntil: 'networkidle' });
    
    for (const vp of viewports) {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      // Wait a moment for layout to adjust
      await page.waitForTimeout(500);
      
      // Capture full page
      await page.screenshot({ 
        path: `screenshots/${route.name}-${vp.name}-full.png`, 
        fullPage: true 
      });
      
      // Capture only the first viewport
      await page.screenshot({ 
        path: `screenshots/${route.name}-${vp.name}-hero.png`, 
        fullPage: false 
      });
    }
    
    await context.close();
  }
  
  await browser.close();
  server.kill();
  console.log("Screenshots captured successfully.");
  process.exit(0);
}, 3000);
