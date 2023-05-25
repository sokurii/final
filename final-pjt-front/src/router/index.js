import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import FinanceView from '../views/FinanceView.vue'
import MapView from '../views/MapView.vue'
import ExchangeView from '../views/ExchangeView.vue'
import CommunityView from '../views/CommunityView.vue'
import ProfileView from '../views/ProfileView.vue'
import DepositProductDetailView from '../views/DepositProductDetailView.vue'
import SavingProductDetailView from '../views/SavingProductDetailView.vue'
import CreateArticleView from '../views/CreateArticleView.vue'
import DetailArticleView from '../views/DetailArticleView.vue'
import UpdateArticleView from '../views/UpdateArticleView.vue'

import store from '../store'

Vue.use(VueRouter)

const isLoggedIn = store.getters.isLogin

const routes = [
  { // 메인 페이지
    path: '/',
    name: 'home',
    component: HomeView
  },
  { // 로그인 페이지
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin === true) {
        alert('이미 로그인이 되어있습니다.')
        next({ name: 'home' })
      } else {
        next()
      }
    }
  },
  { // 회원가입 페이지
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  { // 금융상품조회 페이지
    path: '/finance',
    name: 'finance',
    component: FinanceView
  },
  // { // 정기예금 상품 상세 조회 페이지
  //   path: '/finance/deposit/:fin_prdt_cd',
  //   name: 'depositDetail',
  //   component: DepositProductDetailView
  // },
  // { // 금융상품 상세 조회 페이지
  //   path: '/finance/saving/:fin_prdt_cd',
  //   name: 'savingDetail',
  //   component: SavingProductDetailView
  // },
  { // 지도 페이지
    path: '/map',
    name: 'map',
    component: MapView
  },
  { // 환율 페이지
    path: '/exchange',
    name: 'exchange',
    component: ExchangeView
  },
  { // 게시판 페이지
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  { // 게시글 작성 페이지
    path: '/community/create',
    name: 'CreateArticle',
    component: CreateArticleView
  },
  { // 게시글 상세 페이지
    path: '/community/:id',
    name: 'DetailArticle',
    component: DetailArticleView
  },
  { // 게시글 수정 페이지
    path: '/community/:id/update',
    name: 'UpdateArticle',
    component: UpdateArticleView
  },
  { // 프로필 페이지
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const authPages = [
    'finance',
    'map',
    'exchange',
    'CreateArticle',
    'DetailArticle',
    'UpdateArticle',
    'profile',
  ]

  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인이 필요한 서비스입니다.')
    next({ name: 'login' })
  } else {
    next()
  }
})

export default router
