<template>
  <div>
    <div id="wrap1">
      <div class="container">
        <div id="top-box">
          <div id="image1-wrap">
            <img src="@/assets/2.png" alt="" id="image1">
          </div>
          <div id="signup-wrap" class="mt-4">
            <form @submit.prevent="login(credentials)">
              <div id="input-div">
                <input type="text" class="form-control" placeholder="전화번호 사용자 이름 또는 이메일" v-model="credentials.username" required>
              </div>
              <div id="input-div">
                <input type="password" class="form-control" placeholder="비밀번호" v-model="credentials.password" required>
              </div>
              <div>
                <input type="submit" value="로그인" id="btn2">
              </div>
            </form>
          </div>

          <div class="mt-3" id="text3-wrap">
            <p id="text3">━━━━━━━━━━ 또는  ━━━━━━━━━━</p>
          </div>

          <div id="facebook-login-wrap">
            <img src="@/assets/5.png" alt="" id="image5">
            <a id="text2" href="https://www.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%252214r6x7l1smyh931d6mzpj1ku2i8g1qnz34u1d3vpd418q1hpo10lu6ie%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Dko_KR%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1375b10b-cf1e-4c87-8e94-b4ced2588d1b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252214r6x7l1smyh931d6mzpj1ku2i8g1qnz34u1d3vpd418q1hpo10lu6ie%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=ko_KR&pl_dbl=0"><span>  Facebook으로 로그인</span></a>
          </div>
        </div>

        <div id="bottom-box">
            <span id="text5">계정이 없으신가요?</span><router-link :to="{ name: 'signup'}" id="text5-1"><span id="text5-1">가입하기</span></router-link>
        </div>

        <div id="bottom-box2">
          <span id="text6">앱을 다운로드 하세요.</span>
        </div>
        
        <div id="bottom-box3">
          <a href="https://l.instagram.com/?u=https%3A%2F%2Fitunes.apple.com%2Fapp%2Finstagram%2Fid389801252%3Fpt%3D428156%26ct%3Digweb.loginPage.badge%26mt%3D8%26vt%3Dlo&e=ATNC0MCrrVZzsctbuB-prfjK_65UJItZzatta3qania7hg4y9OAie-q_noc5ep0_n8zJ5ch3ioT9K9Al&s=1"><img src="@/assets/3.png" alt="" id="image3"></a>
          <a href="https://play.google.com/store/apps/details?id=com.instagram.android&referrer=utm_source%3Dinstagramweb%26utm_campaign%3DloginPage%26ig_mid%3D01A6FE85-1E62-414E-8750-CFA21C1E653C%26utm_content%3Dlo%26utm_medium%3Dbadge"><img src="@/assets/4.png" alt="" id="image4"></a>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
	name: 'LoginView',
	data() {
		return {
			credentials: {
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
  height: 95vh;
}

.container {
  width: 350px;
  height: 764px;
  margin: auto;
  padding: 0;
}

#top-box {
  border: 1.5px solid rgb(214, 214, 214);
  width: 348px;
  height: 394px;
  background-color: white;
  margin: auto;
}

#bottom-box {
  border: 1.5px solid rgb(214, 214, 214);
  width: 348px;
  height: 68px;
  background-color: white;
  margin-top: 15px;
}

#image1-wrap {
  text-align: center;
  margin-top: 50px;
}

#text-wrap1 {
  text-align: center;
  margin-top: 20px;
}

#text1 {
  font-weight: bold;
  color: rgb(175, 175, 175);
}

#btn1-wrap {
  text-align: center;
  margin-top: 18px;
}

#btn1 {
  width: 266px;
  height: 33px;
  background-color: #0095f6;
}

#text2 {
  color: #00376b;
  font-weight: bold;
  text-decoration: none;
  font-size: 13px;
}

#image2 {
  margin-bottom: 4px;
}

#text3-wrap {
  text-align: center;
}

#text3 {
  font-size: 12px;
  color: rgb(175, 175, 175);
}

.form-control {
  width: 258px;
  height: 36px;
  background-color: #fafafa;
}

#signup-wrap {
  width: 100%;
  display: inline-block;
  text-align: center;
}

#input-div {
  display: inline-block;
  text-align: center;
  margin-bottom: 5px;
}

::placeholder {
  font-size: 4px;
}

#text4-wrap {
  width: 258px;
  margin: auto;
}

#text4 {
  text-align: center;
  font-size: 11px;
  color: rgb(133, 133, 133);
}

#btn2 {
  margin-top: 15px;
  width: 266px;
  height: 30px;
  background-color: #0095f6; 
  border: 0px;
  border-radius: 3px;
  color: white;
  font-weight: bold;
}

#bottom-box {
  justify-content : center;
  display: flex;
  align-items: center;
}

#text5 {
  margin: 0;
  font-size: 13px;
}

#text5-1 {
  margin: 0;
  color: rgb(0, 153, 255);
  font-size: 13px;
  text-decoration: none;
}

#bottom-box2 {
  margin-top: 20px;
  justify-content : center;
  display: flex;
  align-items: center;
}

#text6 {
  font-size: 13px;
}

#image3 {
  width: 136px;
  height: 40px;
  margin-right: 8px;
}

#image4 {
  width: 136px;
  height: 40px;
}

#bottom-box3 {
  margin-top: 20px;
  text-align: center;
}

#facebook-login-wrap {
  text-align: center;
  margin-top: 25px;
}
</style>