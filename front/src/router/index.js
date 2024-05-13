import { createRouter, createWebHistory } from 'vue-router'
import CommunityView from '@/views/CommunityView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import HomeView from '@/views/HomeView.vue'
import MapsView from '@/views/MapsView.vue'
import MyAccountView from '@/views/MyAccountView.vue'
import ProductCompareView from '@/views/ProductCompareView.vue'
import ProductListView from '@/views/ProductListView.vue'


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
  ]
})

export default router
