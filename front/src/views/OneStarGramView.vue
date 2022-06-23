<template>
  <div>
    <!-- 로그인 되어 있지 않을경우 최초 페이지 렌더링 -->
    <div v-if="!isLoggedIn">
      <first-page></first-page>
    </div>

    <!-- 로그인 되어 있을 경우 게시글 목록 페이지 렌더링 -->
    <div v-if="isLoggedIn">
      <main-page></main-page>
    </div>
  </div>
</template>

<script>
import FirstPage from '@/components/FirstPage.vue'
import MainPage from '@/components/MainPage.vue'

import { mapGetters } from 'vuex'


export default {
  name: 'OneStarGramView',
  components: {
    FirstPage, MainPage

  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>

<style scoped>

</style>