<template>
  <div class="page-search">
    <div class="container">
      <h1 class="title has-text-centered">Search Results</h1>
      <h2 class="subtitle has-text-centered has-text-grey">Search term: "{{ query }}"</h2>

      <div v-if="isLoading" class="has-text-centered">
        <p>Loading...</p>
      </div>

      <div v-if="!isLoading && products.length === 0" class="has-text-centered">
        <p>No products found matching your search.</p>
      </div>

      <div class="columns is-multiline">
        <ProductBox 
          v-for="product in products"
          :key="product.id"
          :product="product"
          class="column is-4" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'

export default {
  name: 'Search',
  components: {
    ProductBox
  },
  data() {
    return {
      products: [],
      query: '',
      isLoading: false
    }
  },
  mounted() {
    document.title = 'Search | ecom'

    let uri = window.location.search.substring(1)
    let params = new URLSearchParams(uri)

    if (params.get('query')) {
      this.query = params.get('query')
      this.performSearch()
    }
  },
  methods: {
    async performSearch() {
      this.isLoading = true

      try {
        const response = await axios.post('/api/v1/products/search/', { 'query': this.query })
        this.products = response.data
      } catch (error) {
        console.error('Search error:', error)
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
</style>
