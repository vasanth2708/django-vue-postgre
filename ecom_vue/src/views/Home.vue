<template>
  <div class="home">
    <section class="hero is-primary is-bold is-large">
      <div class="hero-body has-text-centered">
        <div class="container">
          <h1 class="title">
            My Ecom
          </h1>
          <p class="subtitle">
            Discover Our Latest Products
          </p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="title is-2 has-text-centered">Featured Products</h2>
        <div class="columns is-multiline">
          <ProductBox 
            v-for="product in latestProducts"
            :key="product.id"
            :product="product" />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'

export default {
  name: 'Home',
  components: {
    ProductBox
  },
  data() {
    return {
      latestProducts: []
    }
  },
  mounted() {
    this.getLatestProducts();
    document.title = 'Home | My Ecom';
  },
  methods: {
    async getLatestProducts() {
      try {
        const response = await axios.get('/api/v1/latest-products/');
        this.latestProducts = response.data;
      } catch (error) {
        console.error('Error fetching latest products:', error);
      }
    }
  }
}
</script>

<style scoped>
.hero {
  background-color: #48C774;
}

.section {
  padding: 3rem 1.5rem;
}

@media (max-width: 768px) {
  .hero {
    height: auto;
    padding: 3rem 0;
  }
}
</style>
