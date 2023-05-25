<template>
  <div>
    <h2 class="title">오늘의 환율</h2>
    <p class="date">{{ today }} 기준</p>
    <p class="note">IDR, JPY는 100 화폐단위당 환율</p>
    <hr>
    <div class="exchange-container">
      <ExchangeListItem
        v-for="exchange in exchangesExceptKRW"
        :key="exchange.id"
        :exchange="exchange"
      />
    </div>
    <hr>
  </div>
</template>

<script>
import ExchangeListItem from './ExchangeListItem.vue'

export default {
  name: 'ExchangeList',
  components: {
    ExchangeListItem,
  },
  computed: {
    exchanges() {
      return this.$store.state.exchanges
    },
    exchangesExceptKRW() {
      return this.exchanges.filter(exchange => exchange.cur_unit !== 'KRW')
    },
    today() {
      const today = new Date()
      const year = today.getFullYear() // 현재 연도
      const month = today.getMonth() + 1 // 현재 월 (0부터 시작하므로 1을 더함)
      const day = today.getDate()

      return `${year}-${month}-${day}`
    }
  },
  mounted() {
    this.getExchanges()
  },
  methods: {
    getExchanges() {
      this.$store.dispatch('getExchanges')
    }
  }
}
</script>

<style scoped>
.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.date {
  font-size: 14px;
  margin-bottom: 5px;
}

.note {
  font-size: 12px;
  color: #666;
  margin-bottom: 20px;
}

.exchange-list {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 4px;
}

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 20px 0;
}
</style>
