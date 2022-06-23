<template>
  <div >
    <nav class="navbar navbar-expand-lg navbar-light bg-white mb-5 sticky-top">
      <div class="d-flex flex-row justify-content-between">
        <!-- 이미지 -->
        <div>
          <a class="navbar-brand" href="#">
            <img src="@/assets/2.png" alt="" width="120" height="27" class="mx-5">
          </a>
        </div>
        <!-- 검색바 -->
        <div>
          <form class="d-flex d-none d-sm-block">
            <input class="form-control me-2" type="search" placeholder="검색" aria-label="Search">
          </form>
        </div>

        <!-- 아이콘 -->
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>

</style>
