<template>
  <div>
    <div id="wrap1" class="container">
      <div class="row">
        <div class="d-none d-lg-block col-md-6" id="image-wrapper1">
          <img src="@/assets/11.png" alt="" id="image1">
        </div>
        <div class="col-md-12 col-lg-6" id="box-wrap">
          <div id="top-box">
            <img src="@/assets/2.png" alt="" id="image2">
            <div id="login-form">
              <form @submit.prevent="login(credentials)" class="login-id">
                <div class="mb-2">
                  <input type="text" placeholder="전화번호 사용자 이름 또는 이메일" class="form-control" v-model="credentials.username" required>
                </div>
                <div class="mb-2">
                  <input type="password" placeholder="비밀번호" class="form-control" v-model="credentials.password" required>
                </div>
                <div>
                  <input type="submit" value="로그인" class="btn btn-primary btn-sm">
                </div>
              </form>
              <div class="mt-3">
                <p id="text1">━━━━━━━━━━  또는  ━━━━━━━━━</p>
              </div>
              <div>
                <img src="@/assets/5.png" alt="" id="image5">
                <a id="text2" href="https://www.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%252214r6x7l1smyh931d6mzpj1ku2i8g1qnz34u1d3vpd418q1hpo10lu6ie%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Dko_KR%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1375b10b-cf1e-4c87-8e94-b4ced2588d1b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252214r6x7l1smyh931d6mzpj1ku2i8g1qnz34u1d3vpd418q1hpo10lu6ie%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=ko_KR&pl_dbl=0"><span>  페이스북으로 로그인</span></a>
              </div>
            </div>     
          </div>
          <div id="bottom-box">
            <p id="text3">계정이 없으신가요?</p><router-link :to="{ name: 'signup'}" id="text3-1"><p id="text3-1">가입하기</p></router-link>
          </div>
          <div id="bottom-box2">
            앱을 다운로드하세요.
          </div>
          <div id="bottom-box3">
            <a href="https://l.instagram.com/?u=https%3A%2F%2Fitunes.apple.com%2Fapp%2Finstagram%2Fid389801252%3Fpt%3D428156%26ct%3Digweb.loginPage.badge%26mt%3D8%26vt%3Dlo&e=ATNC0MCrrVZzsctbuB-prfjK_65UJItZzatta3qania7hg4y9OAie-q_noc5ep0_n8zJ5ch3ioT9K9Al&s=1"><img src="@/assets/3.png" alt="" id="image3"></a>
            <a href="https://play.google.com/store/apps/details?id=com.instagram.android&referrer=utm_source%3Dinstagramweb%26utm_campaign%3DloginPage%26ig_mid%3D01A6FE85-1E62-414E-8750-CFA21C1E653C%26utm_content%3Dlo%26utm_medium%3Dbadge"><img src="@/assets/4.png" alt="" id="image4"></a>
          </div>
        </div>
      </div>
    </div>
    <div id="under-var">
      <img src="@/assets/6.png" alt="" id="image6">
      <a id="text4" href="https://github.com/cih831/onestargram"> github</a>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'OneStarGramView',
  data() {
    return {
      credentials : {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style scoped>
#wrap1 {
  margin: auto;
  margin-top: 40px;
  width: 100%;
  height: 85vh;
}

#image-wrapper1 {
  padding: 0;
  text-align: right;
}

#image1 {
  max-width: 340px;
  height: 100%;
}

#box-wrap {
  text-align: left;
}

#top-box {
  border: 1.5px solid rgb(214, 214, 214);
  height: 374px;
  background-color: white;
  width: 350px;
  text-align: center;

}

#bottom-box {
  border: 1.5px solid rgb(214, 214, 214);
  width: 350px;
  margin-top: 17px;
  height: 60px;
  background-color: white;
  justify-content : center;
  display: flex;
  align-items: center;
}

#text3 {
  margin: 0;
  font-size: 13px;
}
#text3-1 {
  margin: 0;
  color: rgb(0, 153, 255);
  font-size: 13px;
  text-decoration: none;
}
#image2 {
  width: 175px;
  height: 51px;
  margin-top: 50px;
}

#bottom-box2 {
  margin-top: 17px;
  width: 350px;
  justify-content : center;
  display: flex;
  align-items: center;
  font-size: 13px;
}



#image3 {
  width: 136px;
  height: 40px;
  margin-top: 20px;
}


#image4 {
  width: 136px;
  height: 40px;
  margin-top: 20px;
  margin-left: 10px;
}


::placeholder {
  font-size: 2px;
}

.form-control {
  width: 268px;
  height: 38px;
  background-color: #fafafa;
}

#login-form {
  margin-top: 40px;
  display: inline-block;
  text-align: center;
}
.btn {
  width: 268px;
}

#text1 {
  font-size: 12px;
  color: rgb(192, 190, 190);
}

#text2 {
  font-size: 12px;
  text-decoration: none;
  color: #00376b;
  font-weight: bold;
}

#image5 {
  width: 16px;
  height: 16px;
}

#under-var {
  text-align: center;
}

#image6 {
  width: 16px;
  height: 16px;
}

#text4 {
  color: rgb(141, 141, 141);
  text-decoration: none;
}


#bottom-box3 {
  width: 350px;
  margin-top: 17px;
  height: 60px;
  justify-content : center;
  display: flex;
  align-items: center;
}
</style>