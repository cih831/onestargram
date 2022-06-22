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
                  <input type="text" placeholder="전화번호 사용자 이름 또는 이메일" class="form-control" required>
                </div>
                <div>
                  <input type="password" placeholder="비밀번호" class="form-control" required>
                </div>
              </form>
            </div>     
          </div>
          <div id="bottom-box">
            <p id="text3">계정이 없으신가요?</p><p id="text3-1"> 가입하기</p>
          </div>
          <div id="bottom-box2">
            앱을 다운로드하세요.
          </div>
          <div id="app-store-img">
            <a href="https://l.instagram.com/?u=https%3A%2F%2Fitunes.apple.com%2Fapp%2Finstagram%2Fid389801252%3Fpt%3D428156%26ct%3Digweb.loginPage.badge%26mt%3D8%26vt%3Dlo&e=ATNC0MCrrVZzsctbuB-prfjK_65UJItZzatta3qania7hg4y9OAie-q_noc5ep0_n8zJ5ch3ioT9K9Al&s=1"><img src="@/assets/3.png" alt="" id="image3"></a>
            <a href="https://play.google.com/store/apps/details?id=com.instagram.android&referrer=utm_source%3Dinstagramweb%26utm_campaign%3DloginPage%26ig_mid%3D01A6FE85-1E62-414E-8750-CFA21C1E653C%26utm_content%3Dlo%26utm_medium%3Dbadge"><img src="@/assets/4.png" alt="" id="image4"></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'OneStarGramView',
}
</script>

<style scoped>
#wrap1 {
  margin: auto;
  width: 60%;
  height: 100vh;

}
#image-wrapper1 {
  padding: 0;
  text-align: center
}

#image1 {
  max-width: 100%;

}


#top-box {
  border: 1.5px solid rgb(214, 214, 214);
  height: 374px;
  background-color: white;
  width: 350px;
  text-align: center;
  margin: auto;
  margin-top:30px;

  margin-left: 0;
}

#bottom-box {
  border: 1.5px solid rgb(214, 214, 214);
  width: 350px;
  margin: auto;
  margin-top: 17px;
  height: 60px;
  background-color: white;
  justify-content : center;
  display: flex;
  align-items: center;

  margin-left: 0;
}

#text3 {
  margin: 0;
  font-size: 13px;
}
#text3-1 {
  margin: 0;
  color: rgb(0, 153, 255);
  font-size: 13px;
}
#image2 {
  width: 175px;
  height: 51px;
  margin-top: 20px;
}

#bottom-box2 {

  margin: auto;
  margin-left: 0;
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

#app-store-img {
  text-align: center;
  width: 350px;
}

::placeholder {
  font-size: 2px;
}

.form-control {
  width: 268px;
  height: 38px;
}

#login-form {
  text-align: center;
  border: 1px solid black;
}
</style>