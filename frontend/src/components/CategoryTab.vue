<template>
  <div class="flex flex-wrap items-center gap-2" ref="tabContainer">
    <button
      v-for="cat in categories"
      :key="cat.id || cat.name"
      @click="$emit('select', cat.name === 'All' ? '' : cat.name)"
      class="relative px-4 py-2 text-sm font-medium rounded-xl transition-all duration-200"
      :class="activeCategory === (cat.name === 'All' ? '' : cat.name)
        ? 'bg-brand-600 text-white shadow-sm shadow-brand-600/20'
        : 'text-slate-500 dark:text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-800/50'"
    >
      {{ cat.name }}
    </button>
  </div>
</template>

<script>
export default {
  name: "CategoryTab",
  props: {
    categories: { type: Array, default: () => [] },
    activeCategory: { type: String, default: '' }
  },
  emits: ['select']
}
</script>
