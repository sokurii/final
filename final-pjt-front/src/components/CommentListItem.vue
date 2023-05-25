<template>
  <div>
    <p>작성자 : {{ comment.username }}</p>
    <div>
      <span> {{ comment.content }} - {{ comment.updated_at.slice(0, 19).replace('T', ' ') }}</span>
      <button class="btn btn-danger" @click="deleteComment">삭제하기</button>
      <button class="btn btn-primary" @click="toggleEditMode">수정하기</button>
      <div v-if="editMode">
        <input v-model="updatedContent" type="text" placeholder="댓글">
        <button class="btn btn-success" @click="updateComment">저장하기</button>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  },
  data() {
    return {
      editMode: false,
      updatedContent: this.comment.content,
    }
  },
  methods: {
    deleteComment() {
      const comment_id = this.comment.id
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${comment_id}/`,
      })
        .then((res) => {
          alert('댓글이 삭제되었습니다.')
          this.$router.go(0)
        })
        .catch(err => console.log(err))
    },
    updateComment() {
      const comment_id = this.comment.id
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/comments/${comment_id}/`,
        data: { content: this.updatedContent }
      })
        .then((res) => {
          alert('댓글이 수정되었습니다.')
          this.editMode = false
          this.$router.go(0)
        })
        .catch(err => console.log(err))
    },
    toggleEditMode() {
      this.editMode = !this.editMode
    },
  }


}
</script>

<style scoped>
span {
  color: black;
}
</style>