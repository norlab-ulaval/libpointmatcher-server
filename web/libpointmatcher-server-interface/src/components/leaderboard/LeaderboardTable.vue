<template>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-3xl font-bold text-center mb-4">libpointmatcher Leaderboard</h1>
      <p class="text-center mb-10">Discover the most effective configurations contributed by our community.</p>
      
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
              <td class="px-6 py-4">{{ entry.date }}</td>
              <td class="px-6 py-4">{{ entry.version }}</td>
              <td class="px-6 py-4">{{ entry.name }}</td>
              <td class="px-6 py-4">{{ entry.score }}</td>
              <td class="px-6 py-4">{{ entry.type }}</td>
            </tr>
          </tbody>
        </table>
      </div>
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
            { date: '2023-03-14', version: '1.3.7', name: 'Delta research', score: 89, type: 'Average' }
        ]
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
  
  