<template>
  <div id="container">
    <form class="signupform mx-auto" @submit.prevent="signUp">
      <div class="signup-container">
        <!-- login-container 왼쪽 요소 -->
          <div class="signup-left">
            <div class="sign-text">Welcome</div>
            <img src="../assets/signupp.png" alt="" class='sign-img'>
          </div>
        <!-- login-container 오른쪽 요소 -->
          <div class = 'signup-right'>
            <div class="input-container">
              <div> 
                <label class="label-text" style="width: 120px;">아이디</label>
                <input type="text"  v-model="id" required style="display: inline-block; ">
              </div>

              <div class="mt-3">
                <label class="label-text" style="width: 120px;">비밀번호</label>
                <input type="password" v-model="password1" required>
              </div>

              <div class="mt-3">
                <label class="label-text" style="width: 120px;">비밀번호 확인</label>
                <input type="password" v-model="password2" required>
              </div>

              <div class="mt-3">
                <label class="label-text " style="width: 120px;">성별</label>
                <b-form-group class="radio-buttons" style="width: 300px; display: inline-block ">
                  <b-form-radio v-model="selectedGender" name="gender" value="male" class="radio-btn">남성</b-form-radio>
                  <b-form-radio v-model="selectedGender" name="gender" value="female" class="radio-btn">여성</b-form-radio>
                </b-form-group>
              </div>

              <div class='mt-3'>
                <label class="label-text" style="width: 120px;">나이</label>
                <select id="age" v-model="selectedAge">
                  <option v-for="age in ages" :key='age' :value="age">{{ age }}</option>
                </select>
              </div>   

              <div class="mt-3">
                <label class="label-text" style="width: 120px;">거주지</label>
                <select id="region" v-model="selectedResidence">
                  <option v-for="region in regions" :key="region" :value="region">{{ region }}</option>
                </select>
              </div>


              <!-- <div class="mt-2 mb-2">
                <div class="label-text" style="width: 120px;">소득??(미정)</div>
              </div>
   -->


              <b-button class="btn btn-warning mt-5" type="submit" style="width: 300px; height:50px;">회원가입</b-button>
              <div class="mt-3">
                <router-link id="login" to="/login">로그인으로 돌아가기</router-link>
              </div>
            </div>
          </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      id: null,
      password1: null,
      password2: null,
      selectedGender: '',
      selectedAge: '',
      selectedResidence: '',
      ages: [
        '10대',
        '20대',
        '30대',
        '40대',
        '50대 이상',
      ],
      regions:[
          '서울특별시',
          '인천광역시',
          '대전광역시',
          '대구광역시',
          '광주광역시',
          '부산광역시',
          '울산광역시',
          '경기도',
          '강원도',
          '충청북도',
          '충청남도',
          '경상북도',
          '경상남도',
          '전라북도',
          '전라남도',
          '제주특별자치도',
      ]
    }
  },
  methods: {
    signUp() {
      const id = this.id  // ID
      const password1 = this.password1  // 비밀번호
      const password2 = this.password2  // 비밀번호 확인
      const selectedGender = this.selectedGender  // 성별
      const selectedAge =this.selectedAge  // 나이
      const selectedResidence = this.selectedResidence  // 거주지

      const payload = {
        id, password1, password2, selectedGender, selectedAge, selectedResidence,
      }
      this.$store.dispatch('signUp', payload)
      
    }
  }
}
</script>

<style scoped>

#container {
  /* padding : 50px ; */
  /* width: 1200px; */
  height: 100vh;
  /* margin: 100px auto ; */
  display: flex;
  flex-grow:1;
  background-color: #F3F2E9;
  /* 배경 이미지 설정 */
  /* background-image: url("../assets/bgc.png");
  background-size: cover; 
  background-position: center;  */
  /* height: calc(100% - 00px); */
}

.signupform{
  width: 60%;
  height: 70%;
  /* position: fixed; */
  /* margin: 0 auto; */
  /* top: 50%;
  left: 50%; */
  /* transform: translate(-50%, -50%); */
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.signup-container{
  display: flex;
  margin: 0 auto;
  justify-content: space-between;
  height: 100%;
  /* background-color: #7ab87d; */
  background-color: #fff;
  border-radius: 20px ;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  
}

/* 왼쪽 */
.signup-left{
  width: 40%;
  background-color: #6da36f;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.sign-text {
  font-size: 70px;
  color: white;
  font-weight: bold;
  position: absolute; /* 추가 */
  top:25%; /* 원하는 위치로 조정 */
  left: 32%; /* 원하는 위치로 조정 */
  transform: translate(-50%, -50%); /* 가운데 정렬 */
}

.sign-img {
  width: 20%;
  position: absolute; /* 추가 */
  top: 60%; /* 원하는 위치로 조정 */
  right: 42%; /* 원하는 위치로 조정 */
  transform: translate(-50%, -50%); /* 가운데 정렬 */
}

/* 오른쪽 */
.signup-right{
  width: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
/* .sign-head{
  font-size: 28px;
  font-weight: bold;
  margin-bottom:40px
} */

.label-text {
  text-align: left;
  font-weight: bold;
}

.right-text{
  font-weight: bold;

}

/* 회원가입 추가 수정  */
input[type="text"], input[type="password"] {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 5px;
  width: 300px; 
  height: 40px;
}

.radio-buttons .radio-btn {
  display: inline-block;
  width: 50%;
  text-align: left;
}

select#age, #region{
  width: 300px;
  height: 40px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>