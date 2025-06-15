<!-- AppHeader.vue -->
<template>
  <div id="app">
    <header>
      <div class="navbar">
        <div class="header-content">
          <div
            class="wrapper2"
            style="background-color: black;"
          >
            <div class="menu-list2dv">
              <ul class="menu-list2">
                <li>
                  <router-link
                    to="/home"
                    class="menu-item2"
                  >
                    Главная
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/about"
                    class="menu-item2"
                  >
                    О нас
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/process"
                    class="menu-item2"
                  >
                    Процесс
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/shop"
                    class="menu-item2"
                  >
                    Магазин
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/contact"
                    class="menu-item2"
                  >
                    Контакты
                  </router-link>
                </li>
              </ul>
            </div>
          </div>

          <div class="wrapper">
            <div
              class="menu"
              style="z-index: 10;"
            >
              <input
                id="burger-checkbox"
                type="checkbox"
                class="burger-checkbox"
              >
              <label
                for="burger-checkbox"
                class="burger"
                style="color: black;"
              />
              <ul
                class="menu-list"
                style="display: none;"
              > 
                <li>
                  <router-link
                    to="/home"
                    class="menu-item"
                  >
                    Главная
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/about"
                    class="menu-item"
                  >
                    О нас
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/process"
                    class="menu-item"
                  >
                    Процесс
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/shop"
                    class="menu-item"
                  >
                    Магазин
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/contact"
                    class="menu-item"
                  >
                    Контакты
                  </router-link>
                </li>
              </ul>
            </div>
          </div>

          

          <div class="Logo">
            <img
              src="@/assets/img/Logo.svg"
              alt="Логотип"
            >
          </div>


          <div class="relative">
      <template v-if="user">
        <!-- Имя пользователя ― кликабельное -->
        <span
          class="cursor-pointer px-3 py-1 hover:bg-gray-700 rounded"
          @click="toggleMenu"
        >
          {{ user.username }}
        </span>
        <!-- выпадающее меню -->
        <div
          v-if="menuOpen"
          class="absolute right-0 mt-2 bg-white text-black rounded shadow p-2 min-w-[150px]"
        >
          <router-link
            to="/profile"
            class="block px-2 py-1 hover:bg-gray-100"
            @click="menuOpen = false"
          >
            Профиль
          </router-link>
          <button
            @click="logout"
            class="w-full text-left px-2 py-1 hover:bg-gray-100"
          >
            Выйти
          </button>
        </div>
      </template>

      <template v-else>
        <router-link to="/login" class="mr-4">Войти</router-link>
        <router-link to="/register">Регистрация</router-link>
      </template>
    </div>
          
        </div>
      </div>
    </header>
  </div>
</template>



<script>
import api from '@/axios'

export default {
  name: 'AppHeader',
  data() {
    return {
      user: null,
      menuOpen: false,
    }
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen
    },
    async fetchUser() {
      const token = localStorage.getItem('access_token')
      if (!token) {
        this.user = null
        return
      }
      try {
        const res = await api.get('/api/user/', {
          headers: { Authorization: `Bearer ${token}` }
        })
        this.user = res.data
      } catch (err) {
        if (err.response?.status === 401) {
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
        }
        this.user = null
      }
    },
    async logout() {
      const refresh = localStorage.getItem('refresh_token')
      try {
        await api.post('/api/logout/', { refresh })
      } catch (_) { /*ignore*/ }
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      this.user = null
      this.menuOpen = false
      this.$router.push('/login')
    }
  },
  mounted() {
    this.fetchUser()
  },
  watch: {
    // если где-то происходит переназначение токенов, можно следить за маршрутом
    $route() {
      this.fetchUser()
    }
  }
}
</script>