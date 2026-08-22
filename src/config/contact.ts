/**
 * Centralized Contact Configuration
 * 
 * IMPORTANT: 
 * - Do NOT commit real personal emails or phone numbers directly to public source control unless explicitly intended to be public.
 * - This configuration handles whether the Contact page displays active communication channels.
 * - If `publicContactEnabled` is false, the site will honestly state that contact is currently closed or restricted.
 */

export const contactConfig = {
  // Master switch to enable/disable public contact channels
  publicContactEnabled: true,
  
  // Direct email address. Leave as empty string to hide.
  email: "support@dealyvip.com",
  
  // WhatsApp number (include country code, no +, no spaces, e.g., 905551234567). Leave as empty string to hide.
  whatsapp: "",
  
  // Optional messaging or portal link. Leave empty to hide.
  messagingLink: ""
};
