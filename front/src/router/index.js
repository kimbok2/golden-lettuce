import { createRouter, createWebHistory } from 'vue-router'
import CommunityView from '@/views/CommunityView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import HomeView from '@/views/HomeView.vue'
import MapsView from '@/views/MapsView.vue'
import MyAccountView from '@/views/MyAccountView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProductCompareView from '@/views/ProductCompareView.vue'
import ProductListView from '@/views/ProductListView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/compare/',
      name: 'compare',
      component: ProductCompareView
    },
    {
      path: '/products/',
      name: 'products',
      component: ProductListView
    },
    {
      path: '/community/',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/maps/',
      name: 'maps',
      component: MapsView
    },
    {
      path: '/user/',
      name: 'user',
      component: MyAccountView
    },
    {
      path: '/exchange/',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/profile/',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/login/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup/',
      name: 'signup',
      component: SignUpView
    },
  ]
})

export default router
