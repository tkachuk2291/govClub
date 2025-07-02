export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  css: [
    'normalize.css/normalize.css'
  ],

  modules: ['@nuxtjs/google-fonts'],

  googleFonts: {
    families: {
      Inter: [400, 500, 700],
    },
    display: 'swap',
  }
})