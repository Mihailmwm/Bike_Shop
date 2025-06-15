<!-- ProfilePage -->
<template>
  <div>
    <!-- Используем компонент Profile, чтобы отобразить данные пользователя -->
    <UserProfile />
  </div>
</template>

<script>
import UserProfile from '@/components/Profile/Profile.vue';


export default {
  name: 'ProfilePage',
  components: {
    UserProfile
  }
}
</script>

<style scoped>
/* Стили для страницы профиля при необходимости */
</style>
