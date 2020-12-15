import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/homepage/HomePage.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePage,
    },
    {
        path: '/goal/daily',
        name: 'DailyGoal',
        component: () => import('../views/goals/daily/DailyGoal.vue')
    },
    {
        path: '/user/profile',
        name: 'UserProfile',
        component: () => import('../views/profile/UserProfile.vue')
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

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})


export default router
