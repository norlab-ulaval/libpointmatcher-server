<template>
    <div class="container mx-auto px-4 pt-8 pb-2">
      <h3 class="text-3xl font-bold text-center mb-4">Previous Evaluations</h3>
      
      <!--<Dataloader  @csv-data="loadCSVData"/>-->
  
      <div class="relative overflow-x-auto" style="min-height: 59vh;">
        <table class="table-fixed w-full text-center text-gray-500 shadow-md sm:rounded-lg">
          <tbody v-if="evaluationEntries" class="text-md">
            <tr v-for="(entry, index) in evaluationEntries" :key="index" class="leaderboard-row bg-white border-b">
              <PreviousEvaluation :runs="entry" :csvData="csvData"/>
            </tr>
          </tbody>
          <tbody v-else>
            <tr>
              <td class="py-4" colspan="5">No evaluations found</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  import PreviousEvaluation from './PreviousEvaluation.vue';
  import Dataloader from '../3d/Dataloader.vue';

  export default {
    name: 'LeaderboardTable',
    components: {
      PreviousEvaluation,
      Dataloader
    },
    data() {
      return {
        evaluationEntries: null,
        csvData: [],
      };
    },
    async created() {
      await this.fetchData();
    },
    methods: {
      async fetchData() {
        /*const response = await getRuns();
        if (response.success) {
          console.log("Response from getRuns...");
          console.log(response.runs);
        } else {
          console.error(response.error);
        }*/

        
        this.evaluationEntries = {
          "123": [
            {
              "run_id": "123",
              "user_email": "jeff",
              "type": "easy",
              "evaluation_name": "one",
              "file_name": "car_cloud400.csv",
              "iterations": [
                {
                  "rotation_error": 0.7,
                  "translation_error": 0.8,
                  "transformation": [                    
                    [
                        0.7083708643913269,
                        0.635924756526947,
                        0.3062828779220581,
                        -0.19353258609771729
                    ],
                    [
                        -0.5084730982780457,
                        0.7607134580612183,
                        -0.4034469723701477,
                        4.999476432800293
                    ],
                    [
                        -0.48955580592155457,
                        0.13005350530147552,
                        0.8622186183929443,
                        4.271844863891602
                    ],
                    [
                        0.0,
                        0.0,
                        0.0,
                        1.0
                    ]                    
                  ]
                },
              ],
              "date": "2021-10-01T00:00:00",
              "anonymous": false,
            },
            {
              "run_id": "123",
              "user_email": "jeff",
              "type": "medium",
              "evaluation_name": "one",
              "file_name": "cloud.csv",
              "iterations": [
                {
                  "rotation_error": 0.6,
                  "translation_error": 0.5,
                  "transformation": [                    
                    [
                        0.7083708643913269,
                        0.635924756526947,
                        0.3062828779220581,
                        -0.19353258609771729
                    ],
                    [
                        -0.5084730982780457,
                        0.7607134580612183,
                        -0.4034469723701477,
                        4.999476432800293
                    ],
                    [
                        -0.48955580592155457,
                        0.13005350530147552,
                        0.8622186183929443,
                        4.271844863891602
                    ],
                    [
                        0.0,
                        0.0,
                        0.0,
                        1.0
                    ]                    
                  ]
                },
              ],
              "date": "2021-10-01T00:00:00",
              "anonymous": false,
            },
            {
              "run_id": "123",
              "user_email": "jeff",
              "type": "hard",
              "evaluation_name": "one",
              "file_name": "cloud.csv",
              "iterations": [
                {
                  "rotation_error": 0.9,
                  "translation_error": 0.8,
                  "transformation": [                    
                    [
                        0.7083708643913269,
                        0.635924756526947,
                        0.3062828779220581,
                        -0.19353258609771729
                    ],
                    [
                        -0.5084730982780457,
                        0.7607134580612183,
                        -0.4034469723701477,
                        4.999476432800293
                    ],
                    [
                        -0.48955580592155457,
                        0.13005350530147552,
                        0.8622186183929443,
                        4.271844863891602
                    ],
                    [
                        0.0,
                        0.0,
                        0.0,
                        1.0
                    ]                           
                  ]
                },
              ],
              "date": "2021-10-01T00:00:00",
              "anonymous": false,
            },
          ],
          "345": [
            {
              "run_id": "345",
              "user_email": "jeff",
              "type": "easy",
              "evaluation_name": "two",
              "file_name": "car_cloud400.csv",
              "iterations": [
                {
                  "rotation_error": 0.7,
                  "translation_error": 0.8,
                  "transformation": [                    
                    [
                        0.7083708643913269,
                        0.635924756526947,
                        0.3062828779220581,
                        -0.19353258609771729
                    ],
                    [
                        -0.5084730982780457,
                        0.7607134580612183,
                        -0.4034469723701477,
                        4.999476432800293
                    ],
                    [
                        -0.48955580592155457,
                        0.13005350530147552,
                        0.8622186183929443,
                        4.271844863891602
                    ],
                    [
                        0.0,
                        0.0,
                        0.0,
                        1.0
                    ]                                        
                  ]
                },
              ],
              "date": "2021-10-01T00:00:00",
              "anonymous": false,
            },
            {
              "run_id": "345",
              "user_email": "jeff",
              "type": "medium",
              "evaluation_name": "two",
              "file_name": "car_cloud400.csv",
              "iterations": [
                {
                  "rotation_error": 0.6,
                  "translation_error": 0.5,
                  "transformation": [                    
                    [
                        0.7083708643913269,
                        0.635924756526947,
                        0.3062828779220581,
                        -0.19353258609771729
                    ],
                    [
                        -0.5084730982780457,
                        0.7607134580612183,
                        -0.4034469723701477,
                        4.999476432800293
                    ],
                    [
                        -0.48955580592155457,
                        0.13005350530147552,
                        0.8622186183929443,
                        4.271844863891602
                    ],
                    [
                        0.0,
                        0.0,
                        0.0,
                        1.0
                    ]                  
                  ]
                },
              ],
              "date": "2021-10-01T00:00:00",
              "anonymous": false,
            },
            {
              "run_id": "345",
              "user_email": "jeff",
              "type": "hard",
              "evaluation_name": "two",
              "file_name": "car_cloud400.csv",
              "iterations": [
                {
                  "rotation_error": 0.9,
                  "translation_error": 0.8,
                  "transformation": [                    
                    [
                        0.7083708643913269,
                        0.635924756526947,
                        0.3062828779220581,
                        -0.19353258609771729
                    ],
                    [
                        -0.5084730982780457,
                        0.7607134580612183,
                        -0.4034469723701477,
                        4.999476432800293
                    ],
                    [
                        -0.48955580592155457,
                        0.13005350530147552,
                        0.8622186183929443,
                        4.271844863891602
                    ],
                    [
                        0.0,
                        0.0,
                        0.0,
                        1.0
                    ]                                       
                  ]
                },
              ],
              "date": "2021-10-01T00:00:00",
              "anonymous": false,
            },        
          ],
        }

        console.log("Inspecting...");
        console.log(this.evaluationEntries);
      },
      loadCSVData(data) {
        this.csvData = data;
      },
      formatDate(dateString) {
        return dateString.split('T')[0];
      },
      capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
      },
      formatScore(score) {
        return (score * 100).toFixed(2);
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
  