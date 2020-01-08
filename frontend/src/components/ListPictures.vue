<template>
  <div class="ListPictures">
    <h2>photos de {{name}}</h2>
    <div id="images_container">
      <img v-for="url of images" v-bind:key="url" v-bind:src="url" alt height="60" width="60" />
    </div>
  </div>
</template>

<script>
export default {
  name: "ListPictures",
  props: ["name", "images"],
  data: () => {
    return {};
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
.images_container{
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}
img{
  margin: 1em;
  border-radius: 0.3em;
}
</style>
