<template>
  <div>
    <div class="nav-container">

      <div class='menu'>       
        <router-link :to="{ name: 'home' }" >
            <img src="./assets/mmop.png" alt="" style="max-width:250px">
        </router-link>
        <router-link :to="{ name: 'home' }">홈</router-link>
        <router-link @click.native="goToLogin" to="/finance">금융상품비교</router-link>
        <router-link @click.native="goToLogin" to="/map">우리동네은행</router-link> 
        <router-link to="/community">커뮤니티</router-link>
        <router-link @click.native="goToLogin" to="/exchange">환율</router-link>
      </div>

      <div class='account'>
        <span v-if="!isLogin">
          <router-link to="/login">로그인</router-link> |
          <router-link :to="{ name: 'signup' }">회원가입</router-link>
        </span>
        <span v-if="isLogin">
          <a href="" @click="logout">로그아웃</a> |
          <router-link :to="{ name: 'profile' }">프로필</router-link>
        </span>
      <!-- </div> -->

      </div>
    </div>

  </div>  

</template>

<script>
// import {mapGetters} from 'vuex'
export default {
    name:'NavBar',
    data(){
        return{

        }
    },
    computed: {
      isLogin() {
        return this.$store.getters.isLogin
      },
    },
    methods: {
      logout() {
        this.$store.commit('SAVE_TOKEN', { token: null, username: null }) // 토큰과 username을 null로 설정하여 로그아웃 처리
        alert('로그아웃 되었습니다!')
        this.$router.push({ name: 'login' }) // 로그인 페이지로 이동
      },

      goToLogin() {
        if (!this.isLogin) {
          alert('로그인이 필요한 서비스입니다.')
          this.$router.push({ name: 'login' })
        }

      },
    },
}
</script>

<style>
    

.nav-container {
  display: flex; /* 주축과 교차축 나눠서 아이템식 */
justify-content: space-between;
background-color: #fff;
width: 100%;
height: 120px;
padding: 0px 200px;
}

/* 내브바 폰트 */
div a {
font-size:19px;
font-weight: bold;
color: black;
text-decoration: none;
}

div a.router-link-exact-active {
  color: #e98f1a;
}



.menu, .account{
display : flex;
justify-content: center;
align-items: center;
gap:25px;

}







</style>