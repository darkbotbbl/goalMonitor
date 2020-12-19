import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/homepage/HomePage.vue'
import Website from "../views/website/Website"

Vue.use(VueRouter)

const routes = [
    // ! -- these routs are for the website aspect of the product
    {
        path: "/",
        component: Website,
        children: [
            {
                path: '/',
                name: 'Home',
                component: HomePage,
            },
            {
                path: '/user/account/login',
                name: 'Login',
                component: () => import('../views/authentication/Login.vue')
            },
            {
                path: '/user/account/signup',
                name: 'Signup',
                component: () => import('../views/authentication/Signup.vue')
            }
        ]
    },
    // ! - these routes are for the main product - the web app
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})


export default router
