import { createRouter, createWebHistory } from "vue-router";
import CommunityView from "@/views/Community/CommunityView.vue";
import CommunityCreateView from "@/views/Community/CommunityCreateView.vue";
import CommunityDetailView from "@/views/Community/CommunityDetailView.vue";
import CommunityHomeView from "@/views/Community/CommunityHomeView.vue";
import CommunityUpdateView from "@/views/Community/CommunityUpdateView.vue";
import ExchangeView from "@/views/ExchangeView.vue";
import HomeView from "@/views/HomeView.vue";
import MapsView from "@/views/MapsView.vue";
import MyAccountView from "@/views/MyAccountView.vue";
import ProfileView from "@/views/Profile/ProfileView.vue";
import ProfileInfoView from "@/views/Profile/ProfileInfoView.vue";
import ProfileUpdateView from "@/views/Profile/ProfileUpdateView.vue";
import ProductCompareView from "@/views/ProductCompareView.vue";
import ProductListView from "@/views/ProductListView.vue";
import LoginView from "@/views/LoginView.vue";
import SignUpView from "@/views/SignUpView.vue";
// 비밀번호 변경
import ProfilePasswordChangeView from "@/views/Profile/ProfilePasswordChangeView.vue";

import { useUserStore } from "@/stores/user";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/compare/",
      name: "compare",
      component: ProductCompareView,
    },
    {
      path: "/products/",
      name: "products",
      component: ProductListView,
    },
    {
      path: "/community/",
      component: CommunityView,
      children: [
        { path: "", name: "community", component: CommunityHomeView },
        {
          path: "create",
          name: "community-create",
          component: CommunityCreateView,
        },
        {
          path: ":id",
          name: "community-detail",
          component: CommunityDetailView,
        },
        {
          path: ":id/update",
          name: "community-update",
          component: CommunityUpdateView,
        },
      ],
    },
    {
      path: "/maps/",
      name: "maps",
      component: MapsView,
    },
    {
      path: "/user/",
      name: "user",
      component: MyAccountView,
    },
    {
      path: "/exchange/",
      name: "exchange",
      component: ExchangeView,
    },
    {
      path: "/profile/",
      component: ProfileView,
      children: [
        { path: "", name: "profile", component: ProfileInfoView },
        {
          path: "update",
          name: "profile-update",
          component: ProfileUpdateView,
        },
        // 비밀번호 변경 뷰
        {
          path: "password_change",
          name: "profile-password-change",
          component: ProfilePasswordChangeView,
        },
      ],
    },
    {
      path: "/login/",
      name: "login",
      component: LoginView,
    },
    {
      path: "/signup/",
      name: "signup",
      component: SignUpView,
    },
  ],
});

// 로그인 없이 접근 가능한 name 정의
const freeAccessNames = [
  "home",
  "compare",
  "products",
  "community",
  "community-detail",
  "maps",
  "exchange",
  "login",
  "signup",
];

// 로그인시 접근 불가능한 name 정의
const loginBlockAccessNames = [
  'login',
  'signup',
]

router.beforeEach((to, from) => {
  const userStore = useUserStore();
  const isLogin = userStore.isLogin;
  // 비로그인 유저에 대해 로그인 필수 페이지 진입시 login alert 창을 띄워주고,
  // 로그인 페이지로 redirect
  if (!freeAccessNames.includes(to.name) && !isLogin) {
    alert("로그인이 필요합니다.");
    router.push({ name: "login" });
  }

});
  if (loginBlockAccessNames.includes(to.name) && isLogin) {
    alert('이미 로그인된 사용자입니다.')
    next(false)
  }
})

export default router;
