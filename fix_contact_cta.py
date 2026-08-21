import re

with open('src/components/ContactCTA.astro', 'r') as f:
    content = f.read()

new_content = """---
export interface Props {
  context?: 'verification' | 'assistance' | 'general';
  lang?: string;
}

const { context = 'general', lang = 'en' } = Astro.props;

const locales = {
  en: {
    generalMessage: "The next step may be further research rather than contacting DealyVIP. Explore our guides to understand the public tools available to you.",
    verificationMessage: "If public information does not answer the practical question, local or professional assistance may sometimes be necessary. We coordinate independent professionals for observation visits.",
    assistanceMessage: "If an observation visit or local coordination is relevant to your needs, review the available contact options.",
    generalBtn: "Prepare Your Information",
    verificationBtn: "Explore Coordination Options",
    assistanceBtn: "Coordinate Local Assistance",
    limitationsBtn: "Understand Limitations",
    contactUrl: "/en/contact/",
    whatWeDoUrl: "/en/what-we-do/"
  },
  tr: {
    generalMessage: "Bir sonraki adım, DealyVIP ile iletişime geçmekten ziyade daha fazla araştırma yapmak olabilir. Açık kaynakları incelemek için rehberlerimizi okuyun.",
    verificationMessage: "Açık kaynaklar pratik sorularınıza yanıt veremiyorsa, yerel veya profesyonel destek gerekebilir. Gözlem ziyaretleri için bağımsız profesyonelleri koordine ediyoruz.",
    assistanceMessage: "Yerinde gözlem ziyareti veya koordinasyon ihtiyacınız varsa iletişim seçeneklerimizi inceleyin.",
    generalBtn: "Bilgilerinizi Hazırlayın",
    verificationBtn: "Koordinasyon Seçeneklerini İnceleyin",
    assistanceBtn: "Yerel Destek Koordine Edin",
    limitationsBtn: "Sınırları Anlayın",
    contactUrl: "/en/contact/", 
    whatWeDoUrl: "/en/what-we-do/"
  },
  uk: {
    generalMessage: "Наступним кроком може бути подальше дослідження замість звернення до DealyVIP. Використовуйте наші посібники.",
    verificationMessage: "Якщо публічної інформації недостатньо, може знадобитися місцева або професійна допомога. Ми координуємо незалежних фахівців.",
    assistanceMessage: "Якщо вам потрібна місцева координація, перегляньте доступні варіанти зв'язку.",
    generalBtn: "Підготуйте інформацію",
    verificationBtn: "Опції координації",
    assistanceBtn: "Місцева підтримка",
    limitationsBtn: "Зрозумійте обмеження",
    contactUrl: "/en/contact/",
    whatWeDoUrl: "/en/what-we-do/"
  }
};

const locale = locales[lang as keyof typeof locales] || locales.en;

let message = locale.generalMessage;
let buttonText = locale.generalBtn;
let showContactBtn = true;

if (context === 'verification') {
  message = locale.verificationMessage;
  buttonText = locale.verificationBtn;
} else if (context === 'assistance') {
  message = locale.assistanceMessage;
  buttonText = locale.assistanceBtn;
}
---
<div style="background: var(--color-slate-50); border: 1px solid var(--color-border); border-radius: 8px; padding: var(--space-lg); margin-top: var(--space-xl); margin-bottom: var(--space-xl);">
  <h3 style="margin-top: 0; margin-bottom: var(--space-sm); font-size: 1.25rem;">
    {lang === 'tr' ? 'Daha Fazla Yardıma mı İhtiyacınız Var?' : (lang === 'uk' ? 'Потрібна додаткова допомога?' : 'Need More Help?')}
  </h3>
  <p style="margin-bottom: var(--space-md); color: var(--color-text-muted); font-size: 0.95rem; line-height: 1.5;">
    {message}
  </p>
  <div style="display: flex; gap: var(--space-sm); flex-wrap: wrap;">
    <a href={locale.whatWeDoUrl} class="no-underline" style="display: inline-block; padding: 0.5rem 1rem; border: 1px solid var(--color-border); border-radius: 4px; background: white; color: var(--color-text); font-weight: 500; font-size: 0.9rem;">
      {locale.limitationsBtn}
    </a>
    {showContactBtn && (
      <a href={locale.contactUrl} class="no-underline" style="display: inline-block; padding: 0.5rem 1rem; background: var(--color-primary); color: white; border-radius: 4px; font-weight: 500; font-size: 0.9rem;">
        {buttonText}
      </a>
    )}
  </div>
</div>
"""
with open('src/components/ContactCTA.astro', 'w') as f:
    f.write(new_content)
