<template>
  <div class="home">
    <header-b-k></header-b-k>
  </div>
</template>

<script lang="ts">
import {defineComponent } from "@vue/composition-api";
import HeaderBK from "@/components/Header/index.vue";

const Home = defineComponent({
  components: {
    HeaderBK
  },
  setup() {
    return {};
  },
});

export default Home;
</script>
