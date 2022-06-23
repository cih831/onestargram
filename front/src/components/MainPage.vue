<template>
  <div class="container">
    <div class="row">
      <!-- 스토리 + 게시글 무한스크롤 -->
      <div class="col-sm-12 col-md-7" id="articles-box">
        <!-- 스토리 -->
        <div id="story-box">

        </div>

        <!-- 게시글 무한스크롤?-->
        <div id="article-box">

        </div>
      </div>
      <!-- 내 계정 + 추천 친구 -->
      <div class="d-none d-sm-block col-md-5" id="recommend-box">
        <div id="user-profile">
          <!-- 프로필사진이있으면 -->
          
          <!-- 프로필사진이없으면 기본 -->
          <!-- current user name 정보 필요 클릭시 마이페이지 이동 -->
          <div id="profile-img-wrap">
            <img src="https://cdn-icons-png.flaticon.com/512/149/149071.png" alt="" id="profile-img">
            <span id="current-user-name">userID</span>
          </div>
        </div>

        <!-- 추천친구찾기 -->
        <div id="recommend-text-wrap">
          <span id="recommend-text1">회원님을 위한 추천</span>
        </div>

        <div id="recommend-user-wrap">
          <div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainPage'
}
</script>

<style scoped>
.container {
  border: 1px solid black;
  height: 100%;
}

#articles-box {
  border: 1px solid black;
  height: 100vh;
  padding: 0;
}

#recommend-box {
  height: 100vh;
  border: 1px solid black;
  padding: 0;
}

#story-box {
  border: 1.95px solid rgb(214, 214, 214);
  border-radius: 5px;
  width: 90%;
  height: 110px;
  margin: auto;
  background-color: white;
}

#profile-img-wrap {
  margin-top: 20px;
  border: 1px solid black;
}

#profile-img {
  width: 70px;
  height: 70px;
}

#current-user-name {
  font-weight: bold;
  margin-left: 20px;
}

#recommend-text1 {
  color: gray;
  font-weight: bold;
  margin-left: 10px;
}

#recommend-text-wrap {
  border: 1px solid black;
  margin-top: 10px;
  margin-bottom: 10px;
}

#recommend-user-wrap {
  border: 1px solid black;
  height: 280px;
}
</style>