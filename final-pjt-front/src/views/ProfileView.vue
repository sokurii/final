<template>
  <div class="profile-page">
    <div class="page-header header-filter" data-parallax="true" style="background-image:url('https://demos.creative-tim.com/bs3/material-kit/assets/img/examples/city.jpg');"></div>
    <b-card no-body>
      <b-tabs pills card vertical>
        <b-tab title="프로필" active>
          <div class="row d-flex justify-content-center align-items-center">
            <div class="col-md-6 ml-auto mr-auto ">
              <div class="profile ">
                <div class="avatar">
                  <img src="../assets/profile.png" alt="Circle Image" class="img-raised rounded-circle img-fluid">
                </div>
                <div class="name">
                  <!-- <h3 class="title">담곰이</h3> -->
                  <h3 class="title">
                    {{ username }}
                    <!-- <span v-if="!showPopup">{{title}}</span> -->
                    <!-- <input v-if="showPopup" class="input" v-model="title"> -->
                    <!-- <button class="btn btn-link" @click="togglePopup('title')">{{ showPopup ? '저장' : '수정'}}</button> -->
                  </h3>
                </div>
              </div>
            </div>
          </div>
          <div class="description text-center">
            <p>{{ content }}</p>
          </div>
          <div v-if="!(profile)">
            프로필을 작성하세요
            <button class="btn btn-primary">프로필 생성</button>
          </div>
          <div v-else>
            <div>
              성별 : {{ profile.gender }}
            </div>
            <div>
              나이 : {{ profile.age }}
            </div>
            <div>
              거주지 : {{ profile.residence }}
            </div>
          </div>
        </b-tab>
        <b-tab title="관심상품">
          <h3 style="font-weight: bold;">총 {{ profile.likedeposits_count + profile.likesavings_count }}개의 관심상품이 있습니다.</h3>
          <hr style="border: none; border-top: 3px solid black;">
          <div class="row d-flex align-items-stretch">
            <div class="col-6">
              <h5 style="font-weight: bold;">정기예금 ({{ profile.likedeposits_count }})</h5>
              <hr>
              <div v-for="deposit in profile.likedeposits" :key="deposit.id">
                <h4>{{ deposit.fin_prdt_nm }}</h4>
                <h6>{{ deposit.kor_co_nm }}</h6>
                <hr>
              </div>
            </div>
            <div class="col-6">
              <h5 style="font-weight: bold;">정기적금 ({{ profile.likesavings_count }})</h5>
              <hr>
              <div v-for="saving in profile.likesavings" :key="saving.id">
                <h4>{{ saving.fin_prdt_nm }}</h4>
                <h6>{{ saving.kor_co_nm }}</h6>
                <hr>
              </div>
            </div>
    
          </div>
        </b-tab>
        <b-tab title="내가 쓴 글">
          <div class="tab-content tab-space">
            <div class="tab-pane work active show" id="work">
              <div>
                <h4 class="title">총 {{ profile.articles_count }}개의 글이 있습니다</h4>
                  <div class="row d-flex justify-content-center align-items-center">
                <!-- <div class="col-md-7 ml-auto mr-auto"> -->
                    <div v-if="!profile.articles_count">
                      게시글을 작성해보세요!
                    </div>
                  <!-- 여기에 게시글 목록 불러와서 붙이기 !!!! -->
                    <div v-else class="row collections">
                    <!-- 게시글 1 -->
                    <div v-for="article in profile.article_set" :key="article.id" class="col-6">
                      <!-- asset에 있는 사진으로 바꾸고 싶은데 왜 안되냐...  -->
                      <div class="card card-background m-2" style="background-image: url('http://www.backdownsouth.com/wp-content/uploads/2016/11/sockfancy004.jpg')">
                        <a href="#pablo"></a>
                        <div class="card-body">
                          <label class="badge">{{ article.created_at.slice(0, 19).replace('T', ' ') }}</label>
                          <a href="#pablo">
                            <h2 class="card-title">
                              <router-link
                              :to="{
                                name: 'DetailArticle', 
                                params: { id: article.id } 
                              }"
                              >
                                {{ article.title }}
                              </router-link>
                            </h2>
                          </a>
                        </div>
                      </div>
                    </div>

                    <!-- 게시글 2 -->
                    <!-- <div class="col-md-6">
                      <div class="card card-background" style="background-image: url('http://www.backdownsouth.com/wp-content/uploads/2016/11/sockfancy004.jpg')">
                        <a href="#pablo"></a>
                        <div class="card-body">
                          <label class="badge">작성 날짜</label>
                          <a href="#pablo">
                            <h2 class="card-title">게시글 제목</h2>
                          </a>
                        </div>
                      </div>
                    </div> -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </b-tab>
      </b-tabs>
    </b-card>
    <!-- 팝업창 -->
    <div class="recommend">
      <div>
        <h1>이런 상품은 어때요?</h1>
      </div>
      <br>
      <br>
      <div class="product-cards row m-4">
        <!-- 카드 목록 -->
        <div v-for="product in randomProducts" :key="product.id" class="col-4">
          <b-card-group deck>
            <b-card
              :header="product.kor_co_nm"
              header-tag="header"
              :title="product.fin_prdt_nm"
            >
              <b-card-text>
                <h6>{{ product.etc_note }}</h6>
              </b-card-text>
              <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
            </b-card>
          </b-card-group>
        </div>
      </div>
    </div>

  </div>



</template>



<script>
export default {
  name: 'ProfileView',
  data(){
    return {
      content: '이 편지는 영국에서 최초로 시작되어...',
      gender: null,
      age: null,
      residence: null,
    }

  },
  computed: {
    username() {
      return this.$store.state.username
    },
    profile() {
      return this.$store.state.profile
    },
    randomProducts() {
      const deposits = this.$store.state.depositProducts;
      const savings = this.$store.state.savingProducts;
      
      const mergedArray = deposits.concat(savings);
      const randomItems = []

      while (randomItems.length < 3 && mergedArray.length > 0) {
        const randomIndex = Math.floor(Math.random() * mergedArray.length)
        const randomItem = mergedArray.splice(randomIndex, 1)[0]
        randomItems.push(randomItem)
      }

      return randomItems
    },
  },
  mounted() {
    this.getMyProfile()
  },
  methods:{
    getMyProfile() {
      const username = this.username
      const payload = {
        username
      }

      this.$store.dispatch('getMyProfile', payload)
    }
  }
};
</script>



<style>
.material-icons {
  /* font-family: 'Material Icons'; */
  font-weight: normal;
  font-style: normal;
  font-size: 24px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
}

/* typography */


.profile-page .page-header {
    height: 380px;
    background-size: cover;
    background-position: center;
    margin: 0;
    padding: 0;
    border: 0;
    display: flex;
    align-items: center;
}

/* 로그인이랑 회원가입 창에 적용해보기  */
/* .header-filter:before {
    position: absolute;
    z-index: 1;
    width: 100%;
    height: 100%;
    display: block;
    left: 0;
    top: 0;
    content: "";
    background: rgba(0,0,0,.5);
} */

.main-container {
    margin: -60px 30px 0;
    border-radius: 6px;
    box-shadow: 0 16px 24px 2px rgba(0,0,0,.14), 0 6px 30px 5px rgba(0,0,0,.12), 0 8px 10px -5px rgba(0,0,0,.2);
}

.main {
    background: #FFF;
    position: relative;
    z-index: 3;
}

.profile-page .profile {
    text-align: center;
}

/* 프로필 이미지 */
.profile-page .profile img {
    max-width: 160px;
    width: 100%;
    margin: 0 auto;
    transform: translate3d(0,-50%,0);
    /* -webkit-transform: translate3d(0,-50%,0); */
    /* -moz-transform: translate3d(0,-50%,0); */
    /* -o-transform: translate3d(0,-50%,0); */
    /* -ms-transform: translate3d(0,-50%,0); */
}

.img-raised {
    box-shadow: 0 5px 15px -8px rgba(0,0,0,.24), 0 8px 10px -5px rgba(0,0,0,.2);
}

.rounded-circle {
    border-radius: 50%!important;
}

/* 게시글 문구 */
.title {
    margin-top: 30px;
    margin-bottom: 25px;
    min-height: 32px;
    color: black;
    font-weight: 700;
    /* font-family: "Roboto Slab","Times New Roman",serif; */
}

.profile-page .description {
    margin: 1.071rem auto 0;
    /* max-width: 600px; */
    max-width: 800px;
    color: #999;
    font-weight: 300;
}

.profile-page .profile .name{
  margin-top: -80px;
}

.profile-page .profile-tabs {
    margin-top: 4.284rem;
}

.nav-pills {
    border: 0;
    border-radius: 3px;
    padding: 0 15px;
}

.nav .nav-item {
    position: relative;
    margin: 0 2px;
}

.nav-pills.nav-pills-icons .nav-item .nav-link {
    border-radius: 4px;
}

.nav-pills .nav-item .nav-link.active {
    color: #fff;
    background-color: #6da36f;
    box-shadow: 0 5px 20px 0 rgba(0,0,0,.2), 0 13px 24px -11px rgba(#6da36f,.6);
}

.nav-pills .nav-item .nav-link {
    line-height: 24px;
    font-size: 12px;
    font-weight: 500;
    min-width: 100px;
    color: #555;
    transition: all .3s;
    border-radius: 30px;
    padding: 10px 15px;
    text-align: center;
}

.nav-pills .nav-item .nav-link:not(.active):hover {
    background-color: rgba(200,200,200,.2);
}


.nav-pills .nav-item i {
    display: block;
    font-size: 30px;
    padding: 15px 0;
}

.tab-space {
    padding: 40px 0 50px;
}

.profile-page .gallery {
    margin-top: 3.213rem;
    padding-bottom: 50px;
}

.profile-page .gallery img {
    width: 100%;
    margin-bottom: 2.142rem;
}

.profile-page .profile .name{
    margin-top: -80px;
}

img.rounded {
    border-radius: 6px!important;
}

.tab-content>.active {
    display: block;
}

.profile-page .follow {
    position: absolute;
    top: 0;
    right: 0;
}

.profile-page .follow .btn-fab {
    margin-top: -28px;
}

.profile-page .work .collections {
    margin-top: 20px;
}

.back-background, .card-background, .front-background {
    background-position: 50%;
    background-size: cover !important;
    text-align: center;
}

.back-background .card-body, .card-background .card-body, .front-background .card-body {
    position: relative;
    z-index: 2;
    min-height: 280px;
    padding-top: 40px;
    padding-bottom: 40px;
    max-width: 440px;
    margin: 0 auto;
}

.profile-page .tab-content .collections .card .card-body .badge {
    display: inline-table;
    margin: 0 auto;
}

.profile-page .work .stats ul>li b {
    font-size: 1.2em;
    color: #3c4858;
}

.profile-page .work .stats ul>li {
    padding: 5px 0;
    font-size: 1em;
    font-weight: 300;
}

.badge {
    padding: 5px 12px;
    text-transform: uppercase;
    font-size: 10px;
    font-weight: 500;
    color: #fff;
    border-radius:.25rem;
}



.back-background .card-title, .card-background .card-title, .front-background .card-title {
    color: #fff;
    margin-top: 10px;
}

.back-background:after, .card-background:after, .front-background:after {
    position: absolute;
    z-index: 1;
    width: 100%;
    height: 100%;
    display: block;
    left: 0;
    top: 0;
    content: "";
    background-color: rgba(0,0,0,.56);
    border-radius: 6px;
}

.card {
    border: 0;
    margin-bottom: 30px;
    margin-top: 30px;
    border-radius: 6px;
    color: rgba(0,0,0,.87);
    background: #fff;
    width: 100%;
    box-shadow: 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.2), 0 1px 5px 0 rgba(0,0,0,.12);
}

.profile-page .tab-content .card .card-body {
    display: flex;
    flex-direction: column;
    justify-content: center;
}


.profile-page  {
    padding: 40px 0;
}

.card-title {
    font-size: 2.25rem !important;
    font-weight: 700 !important;
    /* font-family: Roboto Slab,Times New Roman,serif; */
    color: #3c4858;

}

h4.card-title{
    font-size: 1.125rem !important;
}


.card {
    position: relative;
    padding: 0;
    z-index: 1;
    width: auto;
    margin-left: 15px;
    margin-right: 15px;
    margin-top: -30px;
    border-radius: 6px;
}

.card  a {
    display: block;
}

.card  img {
    width: 100%;
    border-radius: 6px;
    pointer-events: none;
    box-shadow: 0 5px 15px -8px rgba(0,0,0,.24), 0 8px 10px -5px rgba(0,0,0,.2);
}


.card .colored-shadow {
    transform: scale(.94);
    top: 12px;
    filter: blur(12px);
    position: absolute;
    width: 100%;
    height: 100%;
    background-size: cover;
    z-index: -1;
    transition: opacity .45s;
    opacity: 0;
}


.card .card-category {
    margin-top: 10px;
}

.card-description{
  color: #999;
  font-weight: 300;
}




@media screen and (min-width: 767px){
  .card-profile .card-header-image {
      max-height: 215px;
  }
}

@media (max-width: 991px){
.navbar .navbar-translate {
    width: 100%;
    position: relative;
    display: flex;
    -ms-flex-pack: justify!important;
    justify-content: space-between!important;
    -ms-flex-align: center;
    align-items: center;
    -webkit-transition: transform .5s cubic-bezier(.685,.0473,.346,1);
    -moz-transition: transform .5s cubic-bezier(.685,.0473,.346,1);
    -o-transition: transform .5s cubic-bezier(.685,.0473,.346,1);
    -ms-transition: transform .5s cubic-bezier(.685,.0473,.346,1);
    transition: transform .5s cubic-bezier(.685,.0473,.346,1);
}

.navbar-collapse {
    position: fixed;
    display: block;
    top: 0;
    height: 100vh;
    width: 230px;
    right: 0;
    margin-right: 0!important;
    z-index: 1032;
    visibility: visible;
    background-color: #fff;
    overflow-y: visible;
    border-top: none;
    text-align: left;
    padding-right: 0;
    padding-left: 0;
    max-height: none!important;
    -webkit-transform: translate3d(230px,0,0);
    -moz-transform: translate3d(230px,0,0);
    -o-transform: translate3d(230px,0,0);
    -ms-transform: translate3d(230px,0,0);
    transform: translate3d(230px,0,0);
    -webkit-transition: all .5s cubic-bezier(.685,.0473,.346,1);
    -moz-transition: all .5s cubic-bezier(.685,.0473,.346,1);
    -o-transition: all .5s cubic-bezier(.685,.0473,.346,1);
    -ms-transition: all .5s cubic-bezier(.685,.0473,.346,1);
    transition: all .5s cubic-bezier(.685,.0473,.346,1);
}

.navbar-collapse .navbar-nav .nav-item .nav-link {
    color: #3C4858;
    margin: 5px 15px;
}

.navbar-collapse .navbar-nav .nav-item:after {
    width: calc(100% - 30px);
    content: "";
    display: block;
    height: 1px;
    margin-left: 15px;
    background-color: #e5e5e5;
}

.navbar-collapse .dropdown-toggle:after {
    position: absolute;
    right: 16px;
    margin-top: 8px;
}

.navbar .dropdown .dropdown-menu, .navbar .dropdown.show .dropdown-menu {
    background-color: transparent;
    border: 0;
    padding-bottom: 15px;
    transition: none;
    -webkit-box-shadow: none;
    box-shadow: none;
    transform: none!important;
    width: auto;
    margin-bottom: 15px;
    padding-top: 0;
    height: 300px;
    animation: none;
    opacity: 1;
    overflow-y: scroll;
}
.navbar .dropdown-menu .dropdown-item {
    margin-left: 1.5rem;
    margin-right: 1.5rem;
}

.product-cards {
  width: auto;
}

}

</style>