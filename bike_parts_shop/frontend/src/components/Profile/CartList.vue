<template>
  <div>
    <h3 class="text-xl mb-4">Корзина</h3>
    <div v-if="!items.length">Ваша корзина пуста.</div>
    <div class="grid grid-cols-2 gap-4" v-else>
      <ItemCard v-for="item in items" :key="item.product.id" :product="item.product" />
    </div>
  </div>
</template>

<script>
import api from '@/axios'
import ItemCard from '@/components/ShopPage/ItemCard.vue'
export default {
  components: { ItemCard },
  data() { return { items: [] } },
  async mounted() {
    const { data } = await api.get('/api/cart/', this.authHeader())
    this.items = data.items   // структура по вашему сериализатору
  },
  methods: {
    authHeader() {
      const token = localStorage.getItem('access_token')
      return { headers:{ Authorization:`Bearer ${token}` } }
    }
  },
}
</script>
