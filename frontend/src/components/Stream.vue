<template>
  <div class="Stream">
    <!-- <img src="http://192.168.4.4:81/stream" /> -->
    <button @click="whoAmI_alert()">Qui suis-je ?</button>
  </div>

</template>
<script>
import { whoAmI } from "../service";
export default {
  name: "Stream",
  props: {},
  methods: {
    whoAmI_alert: async function() {
      try {
        const name = await whoAmI();
        alert(`bonjour ${name}`);
      } catch {
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
