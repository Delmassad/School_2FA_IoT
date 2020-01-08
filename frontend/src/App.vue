<template>
  <div id="app">
    <img
      alt="Flic"
      height="60"
      width="200"
      src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Logo-police-nationale-france.svg/140px-Logo-police-nationale-france.svg.png"
    />
    <img
      alt="Supélec"
      height="100"
      width="100"
      src="https://upload.wikimedia.org/wikipedia/en/thumb/e/ef/Supelec_logo.svg/150px-Supelec_logo.svg.png"
    />
    <img
      alt="NSA"
      height="100"
      width="100"
      src="https://www.nsa.gov/portals/70/images/about/cryptologic-heritage/center-cryptologic-history/insignia/nsa-insignia-sm.png"
    />
    <h1>Flic de classe</h1>
    <p>Vérification de la présence en cours</p>
    <Stream v-on:newPicture="refreshPicture()" />
    <ListPictures v-show="picturesOf" v-bind:images="picturesURL" v-bind:name="picturesOf" />
    <div>
      <h2>derniere photo prise</h2>
      <img v-if="lastPicture" v-bind:src="lastPicture" />
    </div>
    <ul class="names_container">
      <li v-for="name of names" v-bind:key="name" class="name">
        <div class="name_buttons">
          <button @click="savePictureClick(name)">c'etait moi !</button>
          <button @click="getPicturesOf(name)" v-bind:class="{selected: name === picturesOf}">mes autres photos</button>
        </div>
        {{name}}
      </li>
    </ul>
  </div>
</template>

<script>
/* eslint-disable */
import Stream from "./components/Stream.vue";
import ListPictures from "./components/ListPictures.vue";
import {
  getNames,
  savePicture,
  getPicturesURL,
  getLastPicture
} from "./service";
import { STATIC_URL } from "./env";

export default {
  name: "app",
  components: {
    Stream,
    ListPictures
  },
  data: () => {
    return {
      names: [],
      lastPicture: `${STATIC_URL}/lastPicture/lastPicture.jpeg`,
      picturesOf: "",
      picturesURL: []
    };
  },
  mounted: function() {
    this.refreshPicture();
    getNames().then(n => (this.names = n));
  },
  methods: {
    savePictureClick: function(name) {
      savePicture(name);
    },
    getPicturesOf: async function(name) {
      try {
        this.picturesURL = await getPicturesURL(name);
        this.picturesOf = name;
      } catch {
        console.error(`cannot get file URL for pictures of ${name}`);
      }
    },
    refreshPicture: function() {
      getLastPicture().then(file_name => (this.lastPicture = `${STATIC_URL}/lastPicture/${file_name}`));
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.names_container {
  display: flex;
  flex-direction: column;
  margin-left: 25%;
}
.name {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}
.name_buttons{
  margin-right: 1em;
}
button{
  border-radius: 0.3em;
}button:hover {
  background-color: rgb(159, 191, 228);
}
.selected{
  background-color: rgb(162, 189, 219);
}
</style>
