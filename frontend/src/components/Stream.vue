<template>
  <div class="Stream">
    <img v-bind:src="stream_URL" alt='ESP non connecte'/>
    <button @click="whoAmI_alert()">Qui suis-je ?</button>
  </div>
</template>
<script>
import { whoAmI } from "../service";
import { ESP_URL } from '../env';

export default {
  name: "Stream",
  props: {},
  data: () => {
    return {
      stream_URL: `${ESP_URL}/stream`,
    };
  },
  methods: {
    whoAmI_alert: async function() {
      try {
        const name = await whoAmI();
        this.$emit('newPicture');
        alert(`bonjour ${name}`);
      } catch {
        this.$emit('newPicture');
        alert('je ne te connais pas encore');
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
