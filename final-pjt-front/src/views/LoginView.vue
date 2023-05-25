<template>
  <div id="container">
    <form class="loginform mx-auto" @submit.prevent="login">
      <div class="login-container">
        <!-- login-container 왼쪽 요소 -->
        <div class="login-img">
          <div class=log-text>HELLO🍀<br>모프가 알려주는<br>금융 정보를<br>무료로 즐기세요!</div>
          <div class=log-txt>My Monitoring Planner, MMoP</div>
          <img src="../assets/loginn.png" alt="" class='log-img'>
        </div>
        <!-- login-container 오른쪽 요소 -->
        <div class = 'logininput'>
          <img src="../assets/mmop.png" alt="" class='mmop'>
          <div class="input-container">
            <div> 
              <!-- <b-form-input v-model="text" placeholder="👤 아이디를 입력하세요" style="width: 300px; height:50px;" ></b-form-input> -->
              <b-form-input v-model="id" placeholder="👤 아이디를 입력하세요" style="width: 300px; height:50px;" ></b-form-input>
            </div>
            <div style="margin-top: 10px; margin-bottom:20px;">
              <!-- <b-form-input v-model="text" placeholder="👤 비밀번호를 입력하세요" style="width: 300px; height:50px;"></b-form-input> -->
              <b-form-input type="password" v-model="password" placeholder="🔑 비밀번호를 입력하세요" style="width: 300px; height: 50px;"></b-form-input>
            </div>

            <div class="id-save" style="margin-top: -10px; margin-bottom:20px; width:300px ">
              <b-form-checkbox v-model="rememberId" true-value="true" false-value="false">
                <span style="margin-left: 5px;">아이디 저장</span>
              </b-form-checkbox>
            </div>
              <!-- <input type="checkbox" v-model="rememberId">
              <label for="remember">아이디 저장</label> -->
            <!-- <b-form-checkbox v-model="saveId">아이디 저장</b-form-checkbox> -->
            <b-button class="btn btn-success" type="submit" style="width: 300px; height:50px;">Login</b-button><br>
            <router-link id="signup" to="/signup">회원가입</router-link>

          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
        id: null,
        password: null,
        rememberId: false,
    };
  },

  methods: {
    login() {
      const id = this.id
      const password = this.password

      const payload = {
        id, password
      }
      this.$store.dispatch('logIn', payload)
    }
  },
  // watch: {
  //   rememberId(newVal) {
  //     if (!newVal) {
  //       // 아이디 저장 체크박스가 해제되었을 때, 저장된 아이디를 제거합니다.
  //       localStorage.removeItem('savedId');
  //     } else if (this.id) {
  //       // 아이디 저장 체크박스가 체크되었고, 아이디 입력 필드에 값이 있을 때 아이디를 저장합니다.
  //       localStorage.setItem('savedId', this.id);
  //     }
  //   },
  // },

};
</script>

<style scoped>
#container {
  width: 1200px;
  height: 100vh;
  margin: 100px auto ;
  display: flex;
  flex-grow:1;
}



.loginform{
  width: 70%;
  height: 60%;
}

.login-container {
  display: flex;
  justify-content: space-between;
  height: 100%;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}


.login-img{
  width: 50%;
  background-color: #f8d57b;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.login-img > div{
  position:absolute;
}

.log-img{
  width: 80%;
  opacity : 0.7;
  margin-top: 100px;
  margin-left: 0px;
  
}

.log-text{
  font-size: 27px;
  font-weight: 800;
  z-index: 1;
  text-align: left;
  margin-top: 50px;
  margin-left: 40px;
}

.log-txt{
  font-size:16px;
  font-weight: 400;
  z-index:1;
  margin-top: 215px;
  margin-left: 45px;
}
.logininput{
  width: 50% ;
  
} 

.mmop{
  width:40%;
  margin-top: 50px;
  margin-bottom: 20px;
  margin-left: 50px;
}

.input-container{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items:center;
  height: 70%;
}

.id-save{
  text-align: left;
}
</style>