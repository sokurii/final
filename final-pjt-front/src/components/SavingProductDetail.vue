<template>
  <div>
    <div>
      <b-button v-if="!likeStatusS" pill variant="success" @click="likeSaving">관심상품 등록</b-button>
      <b-button v-else pill @click="likeSaving">관심상품 등록 해제</b-button>
    </div>
    <div class="d-flex flex-column mb-3">
      <div class="p-2 text-start">
        <p>공시 제출월 : {{ product?.dcls_month }}</p>
      </div>
      <div class="p-2 text-start">
        <p>금융회사명 : {{ product?.kor_co_nm }}</p>
      </div>
      <div class="p-2 text-start">
        <p>상품명 : {{ product?.fin_prdt_nm }}</p>
      </div>
      <div class="p-2 text-start">
        <p>가입제한* : {{ product?.join_deny }}</p>
      </div>
      <div class="p-2 text-start">
        <p>가입방법 : {{ product?.join_way }}</p>
      </div>
      <div class="p-2 text-start">
        <p>우대조건 : {{ product?.spcl_cnd }}</p>
      </div>
    </div>
    <div class="d-flex m-4">
      <h6>* 1 - 제한없음, 2 - 서민 전용, 3 - 일부 제한</h6>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SavingProductDetail',
  props: {
    fin_prdt_cd: String,
  },
  data() {
    return {
      product: null,
      likeStatusS: false,
    }
  },
  created() {
    this.getProductDetail()
    this.retrieveLikeStatusS()
  },
  methods: {
    getProductDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/finlife/saving-products/${this.fin_prdt_cd}/`,
      })
        .then((res) => {
          this.product = res.data
        })
        .catch(err => console.log(err))
    },

    retrieveLikeStatusS() {
      const likeStatusS = localStorage.getItem(`likeStatusS_${this.fin_prdt_cd}`)
      if (likeStatusS !== null) {
        this.likeStatusS = JSON.parse(likeStatusS)
      }
    },

    saveLikeStatusS() {
      localStorage.setItem(`likeStatusS_${this.fin_prdt_cd}`, JSON.stringify(this.likeStatusS))
    },
    
    likeSaving() {
      axios({
        method: 'post',
        url: `${API_URL}/finlife/saving-products/${this.fin_prdt_cd}/likes/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
        .then(() => {
          if (!this.likeStatusS) {
            alert('관심상품으로 등록되었습니다.')
            this.likeStatusS = true
          } else {
            alert('관심상품 등록이 해제되었습니다.')
            this.likeStatusS = false
          }

          this.saveLikeStatusS() // like 상태 변경 후 저장
        })
        .catch(err => console.log(err))
    },

    goBack() {
        this.$router.go(-1)
    }
  },
}
</script>

<style>
div h6 {
  font-size: 0.8rem;
}

</style>