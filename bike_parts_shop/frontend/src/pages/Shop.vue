<!-- Shop.vue -->
<template>
  <div class="filca">
    <!-- <ItemFilters v-if="showFilters" @apply-filters="handleFilters" /> -->
    <ProductList :filters="activeFilters" />
  </div>
</template>

<script>
// import ItemFilters from "@/components/ShopPage/ItemFilters.vue";
import ProductList from "@/components/ShopPage/ProductList.vue";

export default {
  name: "ShopPage",
  components: {  ProductList }, //ItemFilters,
  data() {
    return {
      showFilters: true,
      activeFilters: { speed_count: [] }
    };
  },
  methods: {
    handleFilters(filters) {
      console.log("Получены фильтры:", filters);
      // Создаем новый объект для реактивности
      this.activeFilters = { ...filters };
      console.log("Обновленные активные фильтры:", this.activeFilters);
    },
  },
};
</script>


<style scoped>
.filca {
  padding-right: 7vw;
  padding-left: 7vw;
  padding-top: 8em;
    /* display: flex; */
}

  @media (max-width: 768px) {

    .filca {
    /* flex-direction: column; */
}

  }
  @media (min-width: 769px) {  
  
    .filca {

    /* flex-direction: row; */
}
  }
</style>
