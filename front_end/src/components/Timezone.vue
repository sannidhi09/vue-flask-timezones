<template>
  <div class="main">
    <div>
      <h2>Current time now:</h2>
      <h1>{{ current_time }} {{ selected_timezone }}</h1>
    </div>
    <div>
      <h3>Select Time zone:</h3> 
      <select v-model="selected_timezone">
        <option v-for="timezone in time_zones" v-bind:key="timezone" v-bind:value="timezone">
          {{timezone}}
        </option>
      </select>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Timezones',
  data() {
    return {
      time_zones: ['UTC'],
      selected_timezone: 'UTC',
      current_time: ''
    }
  },
  methods: {
    getTimeZones() {
      const path = 'http://localhost:5001/timezones';
      axios.get(path).then((res) => {
        console.log(res.data);
        this.time_zones = res.data.timezones;
        console.log(this.time_zones);
      }).catch((error) => {
        console.error(error);
        alert("Facing issues while fetching the list of timezones from server!!\nClick OK to reload the page.")
        window.location.reload();
        // this.time_zones = ['UTC']
      });
    },
    updateTime() {
      this.current_time = new Date().toLocaleString("en-US",{timeZone: this.selected_timezone});
    }
  },
  created() {
    this.getTimeZones();
  },
  mounted() {
    this.interval = setInterval(()=>{
      this.updateTime();
    }, 500);
  },
  unmounted() {
    clearInterval(this.interval);
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main {
  margin-top: 200px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
