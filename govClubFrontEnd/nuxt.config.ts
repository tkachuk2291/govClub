export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: {enabled: true},
  css: [
    'normalize.css/normalize.css',
    './reset.css',
    '@/assets/styles/global.scss'

  ],

  modules: [
    '@nuxtjs/google-fonts',
    '@nuxtjs/device',
  ],

  googleFonts: {
    families: {
      Inter: [400, 500, 700],
    },
    display: 'swap',
  },
})