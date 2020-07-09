import Vue from 'vue'
// import iView from 'iview'
import iView from 'view-design'
import locale from 'view-design/dist/locale/ru-RU' // Change locale, check node_modules/iview/dist/locale

// import VueLazyload from 'vue-lazyload'

import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

import lodash from 'lodash'

Vue.use(iView, {
  locale
})

Vue.use(VueAwesomeSwiper /* { default options with global component } */)

// Vue.use(VueLazyload, {
//   preLoad: 1.3,
//   error: 'https://via.placeholder.com/300',
//   // eslint-disable-next-line
//   loading: require(`${'@/assets/svg/download.svg'}`),
//   attempt: 3,
//   lazyComponent: true,
//   observer: true,
//   throttleWait: 500
// })

Vue.use(lodash)
