import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

import App from './App.vue'
import router from './router'
import store from './store'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faBars, faMoneyBillWave, faBoxes, faUsersCog, faQuestionCircle, faChartLine, faTimes, faSignInAlt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// Using fontawesome
library.add(faBars, faMoneyBillWave, faBoxes, faUsersCog, faQuestionCircle, faChartLine, faTimes, faSignInAlt)
Vue.component('font-awesome-icon', FontAwesomeIcon)

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

// Vue Axios
Vue.use(VueAxios, axios)

// axios configuration
axios.defaults.withCredentials = true
axios.defaults.baseURL = "http://localhost:8000"

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
