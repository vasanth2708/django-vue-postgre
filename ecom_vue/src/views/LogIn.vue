<template>
  <div class="page-log-in">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Log in</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Username</label>
            <div class="control">
              <input type="text" class="input" v-model.trim="username" required>
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password" required>
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p>{{ errors[0] }}</p> <!-- Display only the first error for simplicity -->
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-dark">Log in</button>
            </div>
          </div>

          <hr>

          Or <router-link to="/sign-up">click here</router-link> to sign up!
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Log In | ecom'
  },
  methods: {
    async submitForm() {
      this.errors = [] // Clear previous errors

      const formData = {
        username: this.username,
        password: this.password
      }

      try {
        const response = await axios.post("/api/v1/token/login/", formData)
        const token = response.data.auth_token

        // Assuming you have a Vuex store with a 'setToken' mutation
        this.$store.commit('setToken', token)

        // Set default auth header for future axios requests
        axios.defaults.headers.common["Authorization"] = `Token ${token}`

        // Store the token in localStorage
        localStorage.setItem("token", token)

        // Redirect the user
        this.$router.push(this.$route.query.redirect || '/dashboard')
      } catch (error) {
        if (error.response && error.response.data) {
          // Assuming the backend returns errors in a consistent format
          const errors = Object.entries(error.response.data)
          this.errors.push(errors.map(([key, value]) => `${key}: ${value}`).join(', '))
        } else {
          this.errors.push('Something went wrong. Please try again')
        }
        console.error(error)
      }
    }
  }
}
</script>
