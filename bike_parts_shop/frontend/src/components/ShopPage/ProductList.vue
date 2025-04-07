<!-- ProductList.vue -->
<template>
  <div class="product-list-container">
    <ItemFilters @apply-filters="handleFilters" />

    <div v-if="loading" class="loading">Загрузка товаров...</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else>
      <div class="products-grid">
        <ItemCard 
          v-for="product in filteredProducts" 
          :key="product.id" 
          :product="product" 
        />
      </div>

      <div v-if="filteredProducts.length === 0" class="no-results">
        Товары по выбранным фильтрам не найдены
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ItemCard from "@/components/ShopPage/ItemCard.vue";
import ItemFilters from "./ItemFilters.vue";

export default {
  name: "ProductList",
  components: { ItemCard, ItemFilters },
  data() {
    return {
      products: [],
      loading: true,
      error: null,
      activeFilters: { 
        speed_count: [] 
      }
    };
  },
  computed: {
    filteredProducts() {
      if (!Array.isArray(this.products)) return [];
      
      return this.products.filter(product => {
        // Проверка по количеству скоростей
        const speedMatch = this.activeFilters.speed_count.length === 0 || 
                         (product.speed_count !== null && 
                          this.activeFilters.speed_count.includes(Number(product.speed_count)));
        
        return speedMatch;
      });
    }
  },
  methods: {
    handleFilters(filters) {
      console.log("Получены фильтры:", filters);
      this.activeFilters = {
        speed_count: [...filters.speed_count]
      };
    }
  },
  async created() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/products/");
      this.products = response.data || [];
    } catch (error) {
      console.error("Ошибка загрузки товаров:", error);
      this.error = "Не удалось загрузить товары. Пожалуйста, попробуйте позже.";
    } finally {
      this.loading = false;
    }
  }
};
</script>

<style scoped>
.product-list-container {
  padding: 20px;
  /* max-width: 1200px; */
  /* margin: 0 auto; */
  /* display: flex; */
}

.loading, .error, .no-results {
  text-align: center;
  padding: 40px;
  font-size: 18px;
  color: #666;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

@media (max-width: 768px) {
  .products-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}

@media (max-width: 480px) {
  .products-grid {
    grid-template-columns: 1fr;
  }
}
</style>