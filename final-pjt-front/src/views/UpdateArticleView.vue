<template>
  <div id="container">
    <div class="board-title d-flex flex-column align-items-center justify-content-center">
      <div><h1 class="board-title-text"><strong>커뮤니티</strong></h1></div>
      <div>Lorem, ipsum dolor sit amet consectetur adipisicing elit.<br>Illum recusandae maxime temporibus blanditiis reprehenderit quos cumque nulla unde sunt</div>
    </div>

    <div class="update-article-container">
      <div class="update-title text-start">
        <h2><strong>게시글 수정</strong></h2>
      </div>      
      <form @submit.prevent="updateArticle" class="update-article-form">
        <label for="title">제목:</label>
        <input type="text" id="title" v-model="title" required><br>
        <label for="content">내용:</label>
        <textarea id="content" cols="30" rows="10" v-model="content" required></textarea><br>
        <div class="submit-btn">
          <button type="submit" id="submit" class="btn btn-success">게시글 수정</button>
        </div>  
      </form>
    </div>  
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateArticleView',
  data() {
    return {
      title: this.$route.params.title,
      content: this.$route.params.content,
    }
  },
  methods: {
    updateArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요!')
        return
      } else if (!content) {
        alert('내용을 입력해주세요!')
        return
      }

      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/update/`,
        data: { title, content },
      })
        .then((res) => {
          alert('게시글이 수정되었습니다.')
          this.$router.push({ name: 'DetailArticle', params: { id: this.$route.params.id } })
        })
        .catch(err => console.log(err))
    },
  }

}
</script>

<style scoped>
.update-article-container {
  background-color: #fff;
  padding: 80px;
  /* height: calc(100% -100px); */
}

.update-article-form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.update-title{
  margin-bottom: 50px;
}

label {
  margin-bottom: 5px;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 10px;
}

button {
  padding: 10px 20px;
}
.btn-success{
  background-color:#6da36f;
  border: none;
}

.submit-btn{
  margin-left: auto;  
}

</style>