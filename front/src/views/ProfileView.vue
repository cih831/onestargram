<template>
  <div class="container">
    <div class="d-flex">
      <div class="box col-3">
        <img v-if="profile.profile_img" :src="profile.profile_img" alt="profile_img">
        <img v-else src="@/assets/profile/base_img.png" alt="profile_img">
      </div>
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

<style>

</style>