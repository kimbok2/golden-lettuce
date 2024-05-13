import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// Pinia Plugin Persisted State
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

// Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'
import * as bootstrap from 'bootstrap'

const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.use(router)

app.mount('#app')
