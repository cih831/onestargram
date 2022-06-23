<template>
  <div>
    <nav v-if="isLoggedIn" class="navbar navbar-expand-lg navbar-light bg-light justify-content-between">
      <ul>
        <router-link :to="{ name: 'onestargram'}"><img src="@/assets/2.png" width="130" height="30" class="mt-2" alt=""></router-link>
      </ul>

      <ul>
        <form class="d-flex">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="검색" id="search-var">
          <!-- <button class="btn btn-outline-primary" type="submit">Search</button> -->
        </form>
      </ul>
      <ul>
        <li>
          <router-link :to="{ name: 'onestargram'}"><img src="@/assets/home1.png" alt="" id="home1"></router-link>
        </li>
        <li>
          <div class="dropdown">
            <button class="dropbtn"><img src="https://cdn-icons-png.flaticon.com/512/149/149071.png" alt="" id="home1"></button>
            <div class="dropdown-content">
              <a><router-link :to="{ name: 'profile', params:{ username:`${currentUser.username}`} }">프로필</router-link></a>
              <a><router-link :to="{ name: 'logout'}">로그아웃</router-link></a>
            </div>
          </div>
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
  },
  methods: {
    ...mapActions(['fetchCurrentUser'])
  },
  created () {
    this.fetchCurrentUser()
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

.dropbtn {
  border: none;
  background-color: rgb(248, 248, 248);

}

.dropdown {
  position: relative;
  display: inline-block;
  margin-left: 20px;
  margin-right: 150px;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: white;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  border-radius: 5px;
}

.dropdown-content a {
  color: black;
  padding: 5px 10px;
  text-decoration: none;
  display: block;
}

.dropdown:hover .dropdown-content {display: block;}

.dropdown-content a:hover {background-color: #ddd;}
</style>
