<template>
  <div v-if="isLoggedIn" >
    <nav class="navbar navbar-expand-lg navbar-light bg-light justify-content-between">
      <li>
        <a class="navbar-brand" href="#">Navbar</a>
      </li>

      <li>
        <form class="d-flex">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </li>
      <li>
        <a class="nav-link active" aria-current="page" href="#">Home</a>
        <a class="nav-link active" aria-current="page" href="#">Home</a>
        <a class="nav-link active" aria-current="page" href="#">Home</a>
      </li>


    </nav>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>

<style scoped>


#search-var {
  width: 300px;
  background-color: rgb(228, 228, 228);
}
</style>
