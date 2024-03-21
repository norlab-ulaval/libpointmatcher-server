<template>
    <div class="container mx-auto px-4 pt-8 pb-2">
      <h1 class="text-3xl font-bold text-center mb-4">libpointmatcher Leaderboard</h1>
      <p class="text-center mb-8">Discover the most effective configurations contributed by our community.</p>
      
      <div class="flex justify-between mb-4">
        <div class="relative">
            <svg class="w-6 h-6 text-gray-800 dark:text-white absolute left-3 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="m21 21-3.5-3.5M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z"/>
            </svg>
            <input
            type="text"
            class="border-2 border-gray-300 bg-white h-10 pl-12 pr-5 rounded-lg text-sm focus:outline-none"
            placeholder="Search..."
            v-model="searchQuery"
            />
        </div>
        <select class="border-2 border-gray-300 bg-white h-10 rounded-lg text-gray-700 w-44 text-center" v-model="selectedType">
            <option value="Average" selected>Average</option>
            <option value="Easy">Easy</option>
            <option value="Hard">Hard</option>
        </select>
      </div>
      
  
      <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <table class="w-full text-left text-gray-500">
          <thead class="text-sm text-gray-700 uppercase" style="background-color: #F1F1F1;">
            <tr>
              <th scope="col" class="px-6 py-3">Date</th>
              <th scope="col" class="px-6 py-3">Release version</th>
              <th scope="col" class="px-6 py-3">Name</th>
              <th scope="col" class="px-6 py-3">Score</th>
              <th scope="col" class="px-6 py-3">Type</th>
            </tr>
          </thead>
          <tbody class="text-md">
            <tr v-for="(entry, index) in filteredLeaderboard" :key="index" class="bg-white border-b">
              <td class="px-6 py-3.5">{{ entry.date }}</td>
              <td class="px-6 py-3.5">{{ entry.version }}</td>
              <td class="px-6 py-3.5">{{ entry.name }}</td>
              <td class="px-6 py-3.5">{{ entry.score }}</td>
              <td class="px-6 py-3.5">{{ entry.type }}</td>
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
          <span class="min-h-[38px] min-w-[38px] flex justify-center items-center border border-gray-200 text-gray-800 py-2 px-3 text-sm rounded-lg focus:outline-none focus:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:border-gray-700 dark:text-white dark:focus:bg-white/10">1</span>
          <span class="min-h-[38px] flex justify-center items-center text-gray-500 py-2 px-1.5 text-sm dark:text-gray-500">of</span>
          <span class="min-h-[38px] flex justify-center items-center text-gray-500 py-2 px-1.5 text-sm dark:text-gray-500">3</span>
        </div>
        <button 
          type="button"
          @click="changePage(currentPage + 1)"
          :disabled="currentPage === totalPages"
          class="min-h-[38px] min-w-[38px] py-2 px-2.5 inline-flex justify-center items-center gap-x-2 text-sm rounded-lg text-gray-800 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:text-white dark:hover:bg-white/10 dark:focus:bg-white/10"
        >
          <span aria-hidden="true" class="sr-only">Next</span>
          <svg class="flex-shrink-0 size-3.5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
        </button>
      </nav>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LeaderboardTable',
    data() {
      return {
        searchQuery: '',
        selectedType: 'Average',
        leaderboard: [
            { date: '2024-02-11', version: '1.0.0', name: 'Anonymous', score: 99, type: 'Average' },
            { date: '2024-01-02', version: '1.8.6', name: 'Anonymous', score: 98, type: 'Average' },
            { date: '2023-12-28', version: '1.9.6', name: 'XYZ Robotics', score: 97.8, type: 'Average' },
            { date: '2023-12-14', version: '1.8.3', name: 'Gamma Industries', score: 97.4, type: 'Average' },
            { date: '2023-11-01', version: '1.9.0', name: 'Beta Solutions', score: 96.9, type: 'Average' },
            { date: '2023-10-21', version: '1.3.8', name: 'Anonymous', score: 96.1, type: 'Average' },
            { date: '2023-10-06', version: '1.1.3', name: 'Alpha tech', score: 94, type: 'Average' },
            { date: '2023-04-02', version: '1.8.1', name: 'John doe', score: 92, type: 'Average' },
            { date: '2023-03-14', version: '1.3.7', name: 'Delta research', score: 89, type: 'Average' },
            { date: '2023-03-14', version: '1.3.7', name: 'Delta research', score: 89, type: 'Average' }
        ],
        currentPage: 1,
        totalPages: 0,
      };
    },
    computed: {
        filteredLeaderboard() {
            return this.leaderboard.filter(entry => {
            const entryValuesString = Object.values(entry).join(' ').toLowerCase();
            return entryValuesString.includes(this.searchQuery.toLowerCase());
            });
        }
    }
  };
  </script>
  
  