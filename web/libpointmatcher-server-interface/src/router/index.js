import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthView from '../views/AuthView.vue'
import About from '../views/AboutView.vue'
import Uploads from '../views/UploadsView.vue'
import ProfileView from '../views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/auth',
      name: 'auth',
      component: AuthView,
    },
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/uploads',
      name: 'uploads',
      component: Uploads
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    }
  ]
})

// router.beforeEach((to, from, next) => {
//   const token = Cookies.get('token');
//   if (token) {
//       try {
//           const decoded = jwtDecode(token);
//           const currentTime = Date.now() / 1000;
//           if (decoded.exp > currentTime) {
//               next();
//           } else {
//               next({ name: 'auth' });
//           }
//       } catch (error) {
//           console.error("Token decoding failed:", error);
//           next({ name: 'auth' });
//       }
//   } else if (to.name !== 'auth') {
//       next({ name: 'auth' });
//   } else {
//       next();
//   }
// });

export default router
