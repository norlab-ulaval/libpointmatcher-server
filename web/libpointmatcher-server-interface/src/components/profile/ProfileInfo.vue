<template>
    <div class="container mx-auto px-4 pt-8 pb-2">
      <h3 class="text-3xl font-bold text-center mb-4 dark:text-gray-100">Previous Evaluations</h3>    
      <div class="relative overflow-x-auto" style="min-height: 59vh;">
        <table v-if="!this.loadingData" class="table-fixed w-full text-center text-gray-500 shadow-md sm:rounded-lg border-separate border-spacing-y-4">
          <tbody v-if="evaluationEntries" class="text-md">
            <tr v-for="(entry, index) in evaluationEntries" :key="index" class="leaderboard-row bg-white border-b rounded-lg overflow-hidden shadow dark:border-b-0">
              <td class="dark:bg-neutral-800 dark:text-gray-100 overflow-hidden">
                <PreviousEvaluation :runs="entry"/>
              </td>
            </tr>
          </tbody>
          <tbody v-else>
            <tr>
              <td class="py-4" colspan="5">No evaluations found</td>
            </tr>
          </tbody>
        </table>
        <div v-else class="text-center">
            <SpinnerIcon></SpinnerIcon>
            <div class="dark:text-gray-200">Loading data...</div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import PreviousEvaluation from './PreviousEvaluation.vue';
  import { getRuns } from '@/api';
  import SpinnerIcon from '@/components/icons/IconSpinner.vue';

  export default {
    name: 'LeaderboardTable',
    components: {
      PreviousEvaluation,  
      SpinnerIcon,
    },
    props: {
      loadingData: {
        type: Boolean,
        required: true,
      },
    },
    data() {
      return {
        evaluationEntries: null,
      };
    },
    async created() {
      await this.fetchData();
    },
    methods: {
      async fetchData() {
        const response = await getRuns();
        if (response.success) {
          this.evaluationEntries = response.runs;
        } else {
          console.error(response.error);
        }     
      },
    },
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
  