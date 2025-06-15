<!-- UserProfile.vue -->
<template>
  <div class="max-w-md mx-auto mt-10 p-6 bg-white rounded shadow">
    <h2 class="text-2xl mb-4">Профиль</h2>
    <p><strong>Имя пользователя:</strong> {{ user.username }}</p>
    <p><strong>Email:</strong> {{ user.email }}</p>

    <button
      @click="logout"
      class="mt-6 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
    >
      Выйти
    </button>
  </div>
</template>

<script>
import api from '@/axios'

export default {
  name: 'UserProfile',
  data() {
    return {
      user: { username: '', email: '' },
    }
  },
  methods: {
    async fetchUser() {
      const token = localStorage.getItem('access_token')
      if (!token) {
        this.$router.push('/login')
        return
      }
      try {
        const res = await api.get('/api/user/', {
          headers: { Authorization: `Bearer ${token}` },
        })
        this.user = res.data
      } catch (error) {
        // Ошибка при получении данных пользователя
        this.$router.push('/login')
      }
    },
    async logout() {
      const refresh = localStorage.getItem('refresh_token')
      try {
        await api.post('/api/logout/', { refresh })
      } catch (error) {
        console.error('Logout error:', error)
      } finally {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        this.$router.push('/login')
      }
    },
  },
  mounted() {
    this.fetchUser()
  },
}
</script>

<style scoped>
/* Добавьте стили, если необходимо */
</style>
