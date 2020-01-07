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
    <Stream />
    <ListPictures v-show="picturesOf" v-bind:images="picturesURL" v-bind:name="picturesOf"/>
    <div>
      <h2>dernier visage détecté</h2>
      <img src="http://127.0.0.1:5000/static/lastPicture/lastPicture.jpeg" alt />
    </div>
    <ul>
      <li v-for="name of names" v-bind:key="name">
        <button @click="savePictureClick(name)">save picture</button>
        <button @click="getPicturesOf(name)">see pictures</button>
        {{name}}
      </li>
    </ul>
  </div>
</template>

<script>
import Stream from "./components/Stream.vue";
import ListPictures from "./components/ListPictures.vue";
import { getNames, savePicture, getPicturesURL } from "./service";

export default {
  name: "app",
  components: {
    Stream,
    ListPictures,
  },
  data: () => {
    return {
      names: [],
      picturesOf: '',
      picturesURL: []
    };
  },
  mounted: function() {
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
</style>
