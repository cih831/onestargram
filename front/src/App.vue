<template>
  <div>
    <!-- 모달창 -->
    <form>
      <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="staticBackdropLabel">새 게시물 만들기</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <h1>사진과 동영상을 여기에 끌어다 놓으세요</h1>
              <input id="upload" type="file" accept="image/*" @change="onInputImage" ref="image" class="upload-box" required>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
              
            </div>
          </div>
        </div>
      </div>
    </form>



    <nav v-if="isLoggedIn" class="navbar navbar-expand-lg navbar-light bg-light justify-content-between">
      <ul>
        <router-link :to="{ name: 'onestargram'}"><img src="@/assets/2.png" width="120" height="30" class="mt-2" alt=""></router-link>
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
          <!-- 모달창 -->
          <img src="@/assets/8.png" alt="" id="home2" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
        </li>
        <li>
          <div class="dropdown">
            <button class="dropbtn"><img src="https://cdn-icons-png.flaticon.com/512/149/149071.png" alt="" id="home1"></button>
            <div class="dropdown-content">
              <a><router-link :to="{ name: 'profile', params:{ username:`${currentUser.username}`} }">프로필</router-link></a>
              <a id="dropdown-table" @click="logout()">로그아웃</a>
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
    ...mapActions(['fetchCurrentUser', 'logout']),
		encodeBase64ImageFile (image) {
      return new Promise((resolve, reject) => {
        let reader = new FileReader()
        reader.readAsDataURL(image[0])
        reader.onload = (event) => {
          resolve(event.target.result)
        }
        reader.onerror = (error) => {
          reject(error)
        }
      })
    },

    onInputImage() {
      this.encodeBase64ImageFile(this.$refs.image.files)
        .then(data => {
          this.cardData.img = data
        })
    },
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
  margin-left: 15px;
  width: 24px;
  height: 24px;
}

#home2 {
  margin-top: 10px;
  margin-left: 15px;
  width: 24px;
  height: 24px;
}

#home2:hover {
  cursor: pointer;
}

.dropbtn {
  border: none;
  background-color: rgb(248, 248, 248);

}

.dropdown {
  position: relative;
  display: inline-block;
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

#dropdown-table {
  padding: 10px;
  padding-left: 20px;
}
</style>
