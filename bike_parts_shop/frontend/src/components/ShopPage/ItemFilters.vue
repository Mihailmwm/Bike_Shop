<!-- ItemFilters.vue -->
<template>
  <div class="filca">
    <div class="filters">
      <h2>Фильтры</h2>
      <div v-for="(category, index) in categories" :key="index" class="category">
        <div @click="toggleCategory(index)" class="category-header">
          {{ category.name }}
          <span>{{ category.open ? '▲' : '▼' }}</span>
        </div>
        <div class="checkbox-group" v-show="category.open">
          <label v-for="(option, i) in category.options" :key="i">
            <input 
              type="checkbox" 
              :value="option" 
              v-model="selectedFilters.speed_count"
            > 
            {{ option }}
          </label>
        </div>
      </div>
      <button @click="applyFilters">Применить</button>
    </div>
  </div>
</template>

<script>
import { ref, reactive } from "vue";

export default {
  name: "ItemFilters",
  emits: ["apply-filters"],
  setup(props, { emit }) {
    const categories = ref([
      { name: "Кареточные коробки", open: false, options: [6, 9, 12] }
    ]);

    const selectedFilters = reactive({ speed_count: [] });

    const toggleCategory = (index) => {
      categories.value[index].open = !categories.value[index].open;
    };

    const applyFilters = () => {
      // Создаем новый объект для передачи
      const filtersToEmit = {
        speed_count: [...selectedFilters.speed_count]
      };
      console.log("Отправляем фильтры:", filtersToEmit);
      emit("apply-filters", filtersToEmit);
    };

    return { 
      categories, 
      selectedFilters, 
      applyFilters, 
      toggleCategory 
    };
  }
};

</script>








<style scoped>

.filca {
  /* padding-right: 7vw;
  padding-left: 7vw;
  padding-top: 8em;
    display: flex; */
}



.filters-container {
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  margin-bottom: 1em;
}

.search-box {
  margin-bottom: 1.5rem;
}

.search-box input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.filter-section {
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #eee;
}

.filter-section h3 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: #333;
}

.price-range {
  margin: 1rem 0;
}

.price-range label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.range-inputs {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.range-inputs input {
  width: 80px;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.availability {
  margin: 1rem 0;
}

.availability label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.category-header {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 0;
  cursor: pointer;
  font-weight: 600;
  color: #2c3e50;
}

.category-header:hover {
  color: #1a73e8;
}

.gear-filter {
  margin-top: 1rem;
  padding-left: 1rem;
}

.gear-filter h4 {
  margin: 0.5rem 0;
  font-size: 0.9rem;
  color: #555;
}

.gear-options {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.gear-options label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  font-size: 0.9rem;
}
</style>