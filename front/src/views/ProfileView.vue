<template>
  <div>
    <div class="container">
      <div class="d-flex">
        <div class="box col-3">
          <img v-if="profile.profile_img" id="profile_img" :src="profile.profile_img" alt="profile_img">
          <img v-else id="profile_img" src="@/assets/profile/base_img.png" alt="profile_img">
        </div>
        <div class="col-8 col-offset-1 container">
          <div>
            <div class="d-flex justify-content-around">
              <h1 v-if="profile.nickname">{{ profile.nickname }}</h1>
              <h1 v-else>{{ profile.username }}</h1>
              <div v-if="isAuthor">
                <router-link :to="{ name: 'profileEdit', params: { username: profile.username}}">
                  <button>Profile Update</button>
                </router-link>
              </div>
              <div v-else>
                <button>Follow User</button>
              </div>
            </div>
            <div>
              <ul class="d-flex">
                <li class="col-2">게시물</li>
                <li class="col-2">팔로워 {{ followersCount }}</li>
                <li class="col-2">팔로우 {{ followingsCount }}</li>
              </ul>
            </div>
            <div>
              <p>introduce</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <div class="d-flex justify-content-center">
      <span>게시물</span>
      <span>저장됨</span>
      <span>태그됨</span>
    </div>
    <hr>
    <div>
      <p>각 컴포넌트 들어갈 자리</p>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  data() {
    return {
      username: this.$route.params.username
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'profile', 'currentUser']),
    followersCount() {
      return this.profile.followers?.length
    },
    followingsCount() {
      return this.profile.followings?.length
    },
  },

  methods: {
    ...mapActions(['fetchProfile', 'followUser'])
  },

  created() {
    const payload = { username: this.$route.params.username}
    this.fetchProfile(payload)
  }
}
</script>

<style scoped>
ul{
  list-style: none;
  padding: 0px;
}

.box {
  width: 150px;
  height: 150px; 
  border-radius: 70%;
  overflow: hidden;
}

#profile_img {
  width: 150px;
  height: 150px;
}

div{
  border: 1px solid black;
  padding: 5px;
}

span{
  border: 1px solid black;
  margin: 5px;
}
</style>