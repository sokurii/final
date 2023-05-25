<template>
  <div>
    <div class="board-title d-flex flex-column align-items-center justify-content-center">
      <div><h1 class="board-title-text"><strong>금융상품비교</strong></h1></div>
      <div>Lorem, ipsum dolor sit amet consectetur adipisicing elit.<br>Illum recusandae maxime temporibus blanditiis reprehenderit quos cumque nulla unde sunt</div>
    </div>

    <b-tabs content-class="bg-white">
      <b-tab title="정기예금" active class="tab">
        <div id="container">
          <DepositProductSearchInput @search-bank="getSearchD"/>
          <DepositProductList :payloadD="payloadD"/>
        </div>
      </b-tab>
      <b-tab title="정기적금">
        <div id="container">
          <SavingProductSearchInput @search-bank="getSearchS"/>
          <SavingProductList :payloadS="payloadS"/>
        </div>
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import DepositProductSearchInput from '@/components/DepositProductSearchInput'
import DepositProductList from '@/components/DepositProductList'
import SavingProductSearchInput from '@/components/SavingProductSearchInput'
import SavingProductList from '@/components/SavingProductList'

export default {
  name: 'FinanceView',
  components: {
    DepositProductSearchInput,
    DepositProductList,
    SavingProductSearchInput,
    SavingProductList,
  },
  data() {
    return {
      payloadD: {},
      payloadS: {},
    }
  },
  methods: {
    getSearchD(payloadD) {
      this.payloadD = payloadD
    },
    getSearchS(payloadS) {
      this.payloadS = payloadS
    },
  }

}
</script>

<style scoped>
.finance{
  background-color: white;
}
#container {
  padding-top: 50px;
  padding-bottom: 90px;
  width: 1200px;
  margin: 0 auto;
  display: flex;
  height: 100vh;
  flex-grow:1;
}

</style>