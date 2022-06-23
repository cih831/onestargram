<template>
  <div>
    <nav v-if="isLoggedIn" class="navbar navbar-expand-lg navbar-light bg-light justify-content-between">
      <ul>
        <a class="navbar-brand" href="#">Navbar</a>
      </ul>

      <ul>
        <form class="d-flex">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="검색" id="search-var">
          <!-- <button class="btn btn-outline-primary" type="submit">Search</button> -->
        </form>
      </ul>
      <ul>
        <li>
          <router-link :to="{ name: 'onestargram'}"><img v-if="isHome" src="@/assets/home2.png" alt="" id="home1"></router-link>
          <router-link :to="{ name: 'onestargram'}"><img v-if="!isHome" src="@/assets/home2.png" alt="" id="home1"></router-link>
        </li>
        <li>
          <a class="nav-link active" aria-current="page" href="#">Login</a>
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn']),
  },
  data() {
    return {
      isHome: false,
    }
  },
  created() {
    let now = window.location.href
    console.log(now)
    if (now === "http://localhost:8080/") {
      this.isHome = true
    }
  }

}
</script>

<style scoped>


#search-var {
  width: 300px;
  background-color: rgb(228, 228, 228);
}

ul {
  list-style: none;
}

li {
  float: left;
}

#home1 {
  margin-top: 10px;
  width: 24px;
  height: 24px;
}
</style>
