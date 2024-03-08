<template>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-3xl font-bold text-center mb-4">libpointmatcher Leaderboard</h1>
      <p class="text-center mb-8">Discover the most effective configurations contributed by our community.</p>
      
      <div class="mb-4">
        <input
          type="text"
          class="border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none"
          placeholder="Search..."
          v-model="searchQuery"
        />
      </div>
  
      <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <table class="w-full text-sm text-left text-gray-500">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50">
            <tr>
              <th scope="col" class="px-6 py-3">Date</th>
              <th scope="col" class="px-6 py-3">Release version</th>
              <th scope="col" class="px-6 py-3">Name</th>
              <th scope="col" class="px-6 py-3">Score</th>
              <th scope="col" class="px-6 py-3">Type</th>
            </tr>
          </thead>
          <tbody>
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
        return this.leaderboard.filter((entry) => {
          return entry.name.toLowerCase().includes(this.searchQuery.toLowerCase());
        });
      }
    }
  };
  </script>
  
  