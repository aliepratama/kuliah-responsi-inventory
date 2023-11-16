import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import('preline')
import { createRouter, createWebHistory } from 'vue-router'

import Home from './routes/Home.vue'
import Products from './routes/Products.vue'
import Forms from './routes/Forms.vue'
import Details from './routes/Details.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        { 
            path: '/', 
            component: Home 
        },
        { 
            path: '/home', 
            component: Home 
        },
        { 
            path: '/products', 
            component: Products 
        },
        { 
            name: 'Create',
            path: '/form', 
            component: Forms 
        },
        { 
            name: 'Details',
            path: '/details/:id', 
            component: Details, 
            props: true 
        },
        { 
            name: 'Edit',
            path: '/edit/:id',
            component: Forms, 
            props: true 
        },
    ]
});
const app = createApp(App)
app.use(router)
app.mount('#app')
