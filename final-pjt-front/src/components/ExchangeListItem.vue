<template>
  <!-- <div>
    <p>통화명 : {{ exchange.cur_unit }} | {{ exchange.cur_nm }} | 환율 : {{ exchange.exchange }}</p>
  </div> -->

  <div>
    <div>
      통화명 : {{ exchange.cur_unit }} | {{ exchange.cur_nm }} | 환율 : {{ exchange.exchange }}
    </div>
  </div>

</template>


<script>
export default {
  name: 'ExchangeListItem',
  props: {
    exchange: Object,
  }
  
}
</script>

<style scoped>
.exchange-container {
  max-height: 100px;
  overflow-y: auto;
  padding: 10px;
  margin-bottom: 10px;
}

.currency-name {
  font-weight: bold;
}

.currency-details {
  margin-left: 10px;
}

.currency-exchange {
  color: #666666;
}
</style>