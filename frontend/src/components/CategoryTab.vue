<template>
  <div class="category-tabs">
    <button 
      v-for="cat in categories" 
      :key="cat" 
      :class="['tab-btn', { active: selectedCategory === cat }]"
      @click="selectCategory(cat)"
    >
      {{ cat }}
    </button>
  </div>
</template>

<script>
export default {
  name: "CategoryTabs",
  data() {
    return {
      categories: ["All", "Tech", "AI", "Lifestyle", "Finance"],
      selectedCategory: "All"
    }
  },
  methods: {
    selectCategory(cat) {
      this.selectedCategory = cat
      this.$emit("categorySelected", cat) // emit to parent
    }
  }
}
</script>

<style scoped>
.category-tabs {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin: 30px 0;
  flex-wrap: wrap;
}

.tab-btn {
  padding: 10px 18px;
  border: none;
  border-radius: 20px;

  color: #000;
  cursor: pointer;
  font-size: 15px;
  transition: all 0.3s ease;
}

.tab-btn:hover {
  background: #ddd;
}

.tab-btn.active {
  background: #ff6600;
  color: white;
  font-weight: bold;
}
</style>
