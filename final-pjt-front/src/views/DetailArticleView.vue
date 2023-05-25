<template>
  <div class="article-details">
    <!-- <div class="board-title d-flex flex-column align-items-center justify-content-center">
      <div><h1 class="board-title-text"><strong>커뮤니티</strong></h1></div>
      <div>Lorem, ipsum dolor sit amet consectetur adipisicing elit.<br>Illum recusandae maxime temporibus blanditiis reprehenderit quos cumque nulla unde sunt</div>
    </div> -->

    <div class="detail-container">
      <h3 class="text-start"><strong>{{ article.title }}</strong></h3>
      <div class="article-info">
        <!-- <p><strong>제목:</strong> {{ article.title }}</p> -->
          <table class="table mt-4">
            <tbody>
              <tr class= "header-title text-start">
                <th style="width: 10%">제목</th>
                <td colspan="3" style="width:90%">{{ article.title }}</td>
              </tr>
              <tr class="text-start">
                <th style="width:10%">작성자</th>
                <td style="width:30%"> {{ article.username }}</td>
                <th style="width:10%">작성 날짜</th>
                <td style="width:40%"> {{ article.created_at.slice(0, 19).replace('T', ' ') }}</td>
              </tr>
              <tr class="height=100%" >
                <td colspan="4" class="p-3 text-start" style="height: 300px">{{ article.content }}</td>
              </tr>
            </tbody>
          </table>
      </div>

      <div class="actions d-flex justify-content-end">
        <router-link
          :to="{
            name: 'UpdateArticle',
            params: { id: article.id, title: article.title, content: article.content },
          }"
        >
          <button class="btn btn-light">수정하기</button>
        </router-link>
        <button class="btn btn-danger" @click="deleteArticle">삭제하기</button>
      </div>
      

      <p class="text-start">댓글 n</p>  <!-- 댓글 n개 있다는 뜻 --> 
      <CommentList :comments="article.comment_set" :id="article.id"/>

      <button class="btn btn-primary" @click="goBack">뒤로가기</button>
    </div>

  </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailArticleView',
  components: {
    CommentList,
  },
  data() {
    return {
      article: {},
    }
  },
  mounted() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios
        .get(`${API_URL}/api/v1/articles/${this.$route.params.id}/`)
        .then((res) => {
          this.article = res.data
        })
        .catch((err) => console.log(err))
    },
    deleteArticle() {
      axios
        .delete(`${API_URL}/api/v1/articles/${this.$route.params.id}/delete/`)
        .then((res) => {
          alert('게시글이 삭제되었습니다.')
          this.$router.push({ name: 'community' })
        })
        .catch((err) => console.log(err))
    },
    goBack() {
      this.$router.push({ name: 'community' })
    },
  },
}
</script>

<style scoped>
/* .article-details{
  /* height: calc(100% - 100px); 
} */

.detail-container{
  margin: 50px auto;
  width: 80%;
  height: calc(100% - 100px);
  background-color: #fff;
  padding: 50px;
  /* border: #ff5555 solid; */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* 그림자 효과 추가 */

}

.header-title{
  border-top: 1px #dfdcdc solid;
}

.article-info{
  height: 100%;
}

/* ------------------------------------- */

.article-details .actions {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.article-details .actions button {
  margin-right: 10px;
}

.article-details .article-info p {
  margin-bottom: 10px;
}

.article-details hr {
  margin-top: 30px;
  border: none;
  border-top: 1px solid #ccc;
}

.article-details .btn-primary {
  margin-top: 20px;
}

/* 추가된 스타일링 */
.article-details p {
  font-size: 16px;
  color: #555;
}

.article-details .btn {
  padding: 8px 16px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
}

.article-details .btn-light {
  background-color: #e2e2e2;
  border: none;
  color: #333;
}

.article-details .btn-danger {
  background-color: #ff5555;
  border: none;
  color: #fff;
}

.article-details .btn-primary {
  background-color: #3366ff;
  border: none;
  color: #fff;
}

.article-details .btn-primary:hover,
.article-details .btn-danger:hover,
.article-details .btn-light:hover {
  opacity: 0.8;
}

/* 테이블 */

.detail-container table {
  width: 100%;
  margin-bottom: 20px;
}

.detail-container th {
  width: 20%;
  background-color: #f0f0f0;
  text-align: left;
}

.detail-container td {
  width: 80%;
}
</style>
