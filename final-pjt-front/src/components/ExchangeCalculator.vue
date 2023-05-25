<template>

<div class="cal-container m-5 p-5 ">
    <h2><strong>환율 계산기</strong></h2>
    <div class="d-flex m-5">
      <div>
        <b-form-select v-model="exchange1" :options="exchangeName"></b-form-select>
        <b-form-input type="number" v-model="exchangeInput" @input="validateInput"></b-form-input>
      </div>
      
      <button class="btn btn-primary" @click="change" style="height:50px">CHANGE</button>

      <div>
        <b-form-select v-model="exchange2" :options="exchangeName"></b-form-select>
        <b-form-input type="number" v-model="exchangeOutput" ></b-form-input>
      </div>
    </div>
</div>

</template>


<script>
export default {
  name: 'ExchangeCalculator',
  data() {
    return {
      exchangeInput: null,
      exchangeOutput: 0,
      exchange1: 'USD 미국 달러',
      exchange2: 'KRW 한국 원',
    }
  },
  computed: {
    exchanges() {
      return this.$store.state.exchanges
    },
    exchangeName() {
      return this.exchanges.map(exchange => exchange.cur_unit + ' ' + exchange.cur_nm)
    },
    exchangeValue() {
      const exchangeValue = {}
      this.exchanges.forEach(exchange => {
        const exchangeKey = exchange.cur_unit + ' ' + exchange.cur_nm
        exchangeValue[exchangeKey] = parseFloat(exchange.exchange.replace(',',''))
      })
      return exchangeValue
    }
  },
  methods: {
    validateInput() {
      // 숫자 이외의 문자 제거
      this.exchangeInput = this.exchangeInput.replace(/[^0-9.]/g, '');
      this.calculateExchange();
    },
    calculateExchange() {
      const exchange1 = this.exchange1
      const exchange2 = this.exchange2
      let exchangeRate = this.exchangeValue[exchange1] / this.exchangeValue[exchange2]

      if (exchange1 === 'JPY(100) 일본 옌' || exchange1 === 'IDR(100) 인도네시아 루피아') {
        exchangeRate = exchangeRate * 0.01
      } 
      if (exchange2 === 'JPY(100) 일본 옌' || exchange2 === 'IDR(100) 인도네시아 루피아'){
        exchangeRate = exchangeRate * 100
      }
      this.exchangeOutput = parseFloat((this.exchangeInput * exchangeRate).toFixed(2))
    },
    change() {
      const temp = this.exchange1
      this.exchange1 = this.exchange2,
      this.exchange2 = temp
      this.exchangeInput = this.exchangeOutput
      this.exchangeOutput = this.exchangeInput * this.exchangeValue[this.exchange1] / this.exchangeValue[this.exchange2]
    }
  }
  
}
</script>

<style scoped>

.cal-container{
  background-color: #6da36f;
  border-radius: 10px;
  height: 300px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
.cal-container > h2{
  color: white;
}

</style>