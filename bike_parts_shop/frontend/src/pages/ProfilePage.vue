<template>
  <div class="profile-page">
    <!-- Вкладки -->
    <div class="tabs">
      <button
        v-for="tab in tabs"
        :key="tab.key"
        @click="currentTab = tab.key"
        :class="['tab-button', { active: currentTab === tab.key }]"
      >
        {{ tab.name }}
      </button>
    </div>

    <!-- Контент вкладки -->
    <div class="tab-content">
      <ProfileInfo v-if="currentTab === 'info'" />
      <OrdersList v-if="currentTab === 'orders'" />
      <CartList v-if="currentTab === 'cart'" />
      <FavoritesList v-if="currentTab === 'favs'" />
    </div>
  </div>
</template>

<script>
import ProfileInfo from '@/components/Profile/ProfileInfo.vue'
import OrdersList from '@/components/Profile/OrdersList.vue'
import CartList from '@/components/Profile/CartList.vue'
import FavoritesList from '@/components/Profile/FavoritesList.vue'

export default {
  name: 'ProfilePage',
  data() {
    return {
      tabs: [
        { key: 'info', name: 'Профиль' },
        { key: 'orders', name: 'Заказы' },
        { key: 'cart', name: 'Корзина' },
        { key: 'favs', name: 'Избранное' },
      ],
      currentTab: 'info',
    }
  },
  components: {
    ProfileInfo,
    OrdersList,
    CartList,
    FavoritesList,
  },
}
</script>

<style scoped>
.profile-page {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.tabs {
  display: flex;
  border-bottom: 2px solid #e5e7eb; /* light gray */
  gap: 1rem;
}

.tab-button {
  background: none;
  border: none;
  padding: 0.5rem 0;
  font-size: 1rem;
  cursor: pointer;
  color: #4b5563; /* gray-600 */
  border-bottom: 2px solid transparent;
  transition: all 0.2s ease-in-out;
}

.tab-button:hover {
  color: #2563eb; /* blue-600 */
}

.tab-button.active {
  color: #2563eb;
  border-color: #2563eb;
}

.tab-content {
  margin-top: 1.5rem;
}
</style>
