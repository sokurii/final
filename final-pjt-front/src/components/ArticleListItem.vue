<template>
  <div>
    <p>
      제목 : 
      <router-link 
      :to="{
        name: 'DetailArticle', 
        params: { id: article.id } 
      }"
      >
        {{ article.title }}
      </router-link> 
    </p>
    <p>작성자 : {{ article.username }}</p>
    <p>날짜 : {{ article.created_at }} </p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>