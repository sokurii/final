<template>
  <div>
    <nav-bar></nav-bar>
    <router-view></router-view>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import NavBar from './NavBar.vue';
  import FootBar from './FootBar.vue';

  export default {
    name:'App',
    components :{
      NavBar,
      FootBar,
    }
    }
  
</script>

<style>
</style>
