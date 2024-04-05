<template>
  <div class="page-cart">
    <div class="columns is-centered">
      <div class="column is-8">
        <h1 class="title has-text-centered">Your Shopping Cart</h1>

        <div class="box" v-if="cartTotalLength">
          <table class="table is-fullwidth is-hoverable">
            <thead>
              <tr>
                <th>Product</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Total</th>
                <th></th>
              </tr>
            </thead>

            <tbody>
              <CartItem
                v-for="item in cart.items"
                :key="item.product.id"
                :initialItem="item"
                @removeFromCart="removeFromCart" />
            </tbody>
          </table>
        </div>

        <p class="has-text-centered" v-else>Your cart is empty...</p>

        <div class="box total-summary">
          <h2 class="subtitle">Total Summary</h2>

          <p><strong>Total:</strong> ${{ cartTotalPrice.toFixed(2) }}</p>
          <p><strong>Items:</strong> {{ cartTotalLength }}</p>

          <hr>

          <div class="buttons is-centered">
            <router-link to="/cart/checkout" class="button is-primary">Proceed to Checkout</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'

export default {
  name: 'Cart',
  components: {
    CartItem
  },
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
    }
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => acc + curVal.quantity, 0)
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => acc + curVal.product.price * curVal.quantity, 0)
    }
  }
}
</script>

<style scoped>
.page-cart {
  padding: 2rem 0;
}

.box {
  margin-bottom: 2rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border: none;
}

.total-summary {
  background-color: #f0f0f0;
}

.table th {
  background-color: #fafafa;
}

.button.is-primary {
  background-color: #3273dc;
  color: #fff;
}

.button.is-primary:hover {
  background-color: #276cda;
}

.buttons.is-centered {
  display: flex;
  justify-content: center;
}
</style>
