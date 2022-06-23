<template>
  <div>

    <div v-if="isLoggedIn">
      <main-page></main-page>
    </div>

    <div v-if="!isLoggedIn">
      <first-page></first-page>
    </div>

    <router-view/>
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
  },
  mounted() {
    console.log(1)
  }
}
</script>

<style scoped>

</style>