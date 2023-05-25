<template>
  <div>
    <div class="board-title d-flex flex-column align-items-center justify-content-center">
      <div><h1 class="board-title-text"><strong>커뮤니티</strong></h1></div>
      <div>Lorem, ipsum dolor sit amet consectetur adipisicing elit.<br>Illum recusandae maxime temporibus blanditiis reprehenderit quos cumque nulla unde sunt</div>
      <!-- <img src="@/assets/document.png"  style="width : 10% ; transform:rotate(20deg);" > -->
    </div>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'CommunityView',
  components: {
    ArticleList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스입니다!')
        this.$router.push({ name: 'login' })
      }
    }
  }
}
</script>

<style>

</style>
