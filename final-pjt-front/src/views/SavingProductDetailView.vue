<template>
  <div>
    <h1 class="d-flex m-4">상품 상세 정보</h1>
    <div>
      <b-button pill variant="success">관심상품 등록</b-button>
      <b-button pill>관심상품 등록 해제</b-button>
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
    <button class="btn btn-primary" @click="goBack">뒤로가기</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SavingProductDetailView',
  data() {
    return {
      product: null
    }
  },
  created() {
    this.getProductDetail()
  },
  methods: {
    getProductDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/finlife/saving-products/${this.$route.params.fin_prdt_cd}/`,
      })
        .then((res) => {
          this.product = res.data
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