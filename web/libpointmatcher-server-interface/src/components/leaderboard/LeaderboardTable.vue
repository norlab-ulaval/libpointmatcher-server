<template>
    <div class="container mx-auto px-4 pt-8 pb-2 ">
      <h1 class="text-3xl font-bold text-center mb-4 dark:text-gray-100">libpointmatcher Leaderboard</h1>
      <p class="text-center mb-8 dark:text-gray-200">Discover the most effective configurations contributed by our community.</p>
      
      <div class="flex justify-between mb-4">
        <div class="relative">
            <svg class="w-6 h-6 text-gray-800 dark:text-white absolute left-3 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="m21 21-3.5-3.5M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z"/>
            </svg>
            <input
            type="text"
            class="border-2 border-gray-300 bg-white h-10 pl-12 pr-5 rounded-lg text-sm focus:outline-none dark:bg-neutral-800 dark:text-gray-100 dark:border dark:border-gray-200"
            placeholder="Search..."
            v-model="searchQuery"
            />
        </div>
        <select class="border-2 border-gray-300 bg-white h-10 rounded-lg text-gray-700 w-44 text-center dark:bg-neutral-800 dark:text-gray-100 dark:border dark:border-gray-200" v-model="selectedType">
          <option value="" disabled>Score type</option>         
          <option value="all">All</option>
          <option v-for="type in scoreTypes" :key="type" :value="type.toLowerCase()">
            {{ capitalizeFirstLetter(type) }}
          </option>
        </select>
      </div>
      
  
      <div class="relative overflow-x-auto" style="min-height: 59vh;">
        <table class="table-fixed w-full text-center text-gray-500 shadow-md sm:rounded-lg dark:border-neutral-800">
          <thead class="text-sm text-gray-700 uppercase bg-gray-100 dark:bg-neutral-800 dark:text-gray-100 dark:text-base">
            <tr>
              <th scope="col" class="w-1/8 px-6 py-3">Date</th>
              <th scope="col" class="w-1/8 px-6 py-3">Release version</th>
              <th scope="col" class="w-1/4 px-6 py-3">User email</th>
              <th scope="col" class="w-1/8 px-6 py-3">Rotation error</th>
              <th scope="col" class="w-1/8 px-6 py-3">Translation error</th>
              <th scope="col" class="w-1/8 px-6 py-3">Type</th>
            </tr>
          </thead>
          <tbody class="text-md">
            <tr v-for="(entry, index) in filteredLeaderboard" :key="index" class="leaderboard-row bg-white border-b dark:bg-neutral-900 dark:border-neutral-700 dark:text-gray-200 dark:border">
              <td class="px-6 py-3.5">{{ formatDate(entry.date) }}</td>
              <td class="px-6 py-3.5">{{ entry.release_version }}</td>
              <td class="px-6 py-3.5">
                <span :class="{'italic': !entry.user_email}">
                  {{ entry.user_email || 'hidden username' }}
                </span>
              </td>
              <td class="px-6 py-3.5">{{ formatScore(entry.rotation_error) }}</td>
              <td class="px-6 py-3.5">{{ formatScore(entry.translation_error) }}</td>
              <td class="px-6 py-3.5">{{ capitalizeFirstLetter(entry.type) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <nav class="flex justify-center items-center gap-x-1 mt-2">
        <button type="button"
          @click="changePage(currentPage - 1)"
          :disabled="currentPage === 1"
          class="min-h-[38px] min-w-[38px] py-2 px-2.5 inline-flex justify-center items-center gap-x-2 text-sm rounded-lg text-gray-800 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:text-white dark:hover:bg-white/10 dark:focus:bg-white/10"
        >
          <svg class="flex-shrink-0 size-3.5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
          <span aria-hidden="true" class="sr-only">Previous</span>
        </button>
        <div class="flex items-center gap-x-1">
          <input
            type="text"
            class="min-h-[38px] w-12 flex justify-center items-center border border-gray-200 text-gray-800 py-2 px-3 text-sm rounded-lg focus:outline-none dark:bg-neutral-800 dark:text-gray-200"
            v-model="inputPage"
            @change="validateAndChangePage"
          />

          <span class="min-h-[38px] flex justify-center items-center text-gray-500 py-2 px-1.5 text-sm dark:text-gray-500">
            of
          </span>
          <span class="min-h-[38px] flex justify-center items-center text-gray-500 py-2 px-1.5 text-sm dark:text-gray-500">
            {{ total }}
          </span>
        </div>
        <button 
          type="button"
          @click="changePage(currentPage + 1)"
          :disabled="currentPage === total"
          class="min-h-[38px] min-w-[38px] py-2 px-2.5 inline-flex justify-center items-center gap-x-2 text-sm rounded-lg text-gray-800 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:text-white dark:hover:bg-white/10 dark:focus:bg-white/10"
        >
          <span aria-hidden="true" class="sr-only">Next</span>
          <svg class="flex-shrink-0 size-3.5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
        </button>
      </nav>
    </div>
  </template>
  
  <script>
  import { getLeaderboard, getScoreTypes } from '@/api';

  export default {
    name: 'LeaderboardTable',
    data() {
      return {
        searchQuery: '',
        selectedType: 'all',
        scoreTypes: [],
        leaderboardEntries: [],
        currentPage: 1,
        total: 1,
        limit: 10,
        inputPage: 1,
        showDropdown: false,
        placeholder: 'Score type',
      };
    },
    async created() {
      await this.fetchData();
      await this.fetchScoreTypes();
    },
    methods: {
      async fetchData() {
        const response = await getLeaderboard(this.currentPage, this.limit, this.selectedType);
        if (response.success) {
          this.leaderboardEntries = response.leaderboard.entries;
          this.total = Math.ceil(response.leaderboard.total / this.limit);
        } else {
          console.error(response.error);
        }
      },
      validateAndChangePage() {
        const page = parseInt(this.inputPage, 10);
        if (!isNaN(page) && page >= 1 && page <= this.total) {
          this.currentPage = page;
          this.fetchData();
        } else {
          this.inputPage = this.currentPage;
        }
      },
      formatDate(dateString) {
        return dateString.split('T')[0];
      },
      async fetchScoreTypes() {
        const response = await getScoreTypes();
        if (response.success) {
          this.scoreTypes = response.types;
        } else {
          console.error(response.error);
        }
      },
      capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
      },
      formatScore(score) {
        return score.toFixed(2);
      },
    },
    watch: {
      selectedType() {
        this.currentPage = 1;
        this.fetchData();
      }
    },
    computed: {
        filteredLeaderboard() {
            return this.leaderboardEntries.filter(entry => {
            const entryValuesString = Object.values(entry).join(' ').toLowerCase();
            return entryValuesString.includes(this.searchQuery.toLowerCase());
            });
        }
    }
  };
  </script>
  
<style>
  .min-height-leaderboard {
    min-height: 59vh;
  }
  .custom-min-width {
    min-width: 10px;
  }

  .leaderboard-row {
    min-height: 5rem;
  }

  tbody::after {
    content: '';
    display: block;
    line-height: 5rem;
  }

  @media (min-width: 640px) {
    .leaderboard-row {
      min-height: 5rem;
    }

    tbody::after {
      line-height: 5rem;
    }

  }
</style>
  