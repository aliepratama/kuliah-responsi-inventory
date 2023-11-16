/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,vue}",
  'node_modules/preline/dist/*.js',],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['"Plus Jakarta Sans"']
      }
    },
  },
  plugins: [
    require('preline/plugin'),
  ],
  darkMode: 'false',
}

