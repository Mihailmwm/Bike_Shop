<!-- ProductList.vue -->

<template>
  <div class="product-list-container">
    <!-- <ItemFilters @apply-filters="handleFilters" /> -->

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

export default {
  components: { ItemCard },
  props: {
    filters: {
      type: Object,
      required: true,
      default: () => ({ 
        speed_count: [] 
      })
    }
  },
  data() {
    return {
      products: [],
      loading: true,
      error: null
    };
  },
  computed: {
    filteredProducts() {
      // Защита от undefined
      if (!Array.isArray(this.products)) return [];
      
      // Создаем копию массива для фильтрации
      return this.products.filter(product => {
        
        // Проверяем соответствие количеству передач
        const matchesSpeed = this.filters.speed_count.length === 0 || 
          (product.speed_count !== null && 
           this.filters.speed_count.includes(Number(product.speed_count)));
        
        return matchesSpeed;
      });
    },
  },

  async created() {
    this.loading = true;
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/products/");
      this.products = response.data || [];
    } catch (error) {
      console.error("Ошибка загрузки товаров:", error);
      this.error = "Не удалось загрузить товары";
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style scoped>
/* .products {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
} */

.products {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  /* justify-content: ;  */
  justify-content: space-between;
}

.card {
  /* flex: 1 1 calc(33.333% - 20px);  */
  /* max-width: calc(33.333% - 20px); */
  /* box-sizing: border-box;
  border: 1px solid #ddd;
  padding: 15px;
  text-align: center;
  background: #fff;
  border-radius: 8px; */
}

/* Для планшетов */
@media (max-width: 1024px) {
  .card {
    flex: 1 1 calc(50% - 20px); /* Две карточки в ряд */
    max-width: calc(50% - 20px);
  }
}

/* Для мобильных */
@media (max-width: 768px) {
  .card {
    flex: 1 1 100%; /* Одна карточка в ряд */
    max-width: 100%;
    max-width: calc(50% - 20px);
  }
}
</style>





<!-- <script>
import ItemCard from "@/components/ShopPage/ItemCard.vue";

export default {
  components: { ItemCard },
  props: {
    filters: {
      type: Object,
      default: () => ({ speed_count: [] }),
    },
  },
  data() {
    return {
      products: [],
    };
  },
  computed: {
    filteredProducts() {
      if (this.filters.speed_count.length === 0) {
        return this.products;
      }
      return this.products.filter((product) =>
        this.filters.speed_count.includes(Number(product.speed_count))
      );
    },
  },
};
</script> -->