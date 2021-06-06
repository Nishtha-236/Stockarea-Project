<template>
  <div>
    <div class="home" style="display:flex">
      <div class="container warehouse">
        <img src="@/images.jpg" class="image1">
        <div @click="details(warehouse.id)" class="middle">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
        </div>
        <div class="bg-white data" @click="details(warehouse.id)" style="width:250px;">
          <div>{{warehouse.name}}</div>
          <div>{{warehouse.city}}</div>
          <div>{{warehouse.cluster}}</div>
          <div>{{warehouse.space_available}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  props:["warehouse"],
  
  data(){
    return{
      
    }
  },
  methods:{
    details(val){
      this.$router.push({name: 'About',params:{id:val}});
    },
  }
}
</script>


<style>
  .home {
    width: 250px;
    float: left;
    margin: 25px 0px 25px 100px;
    -webkit-filter: drop-shadow(1px 1px 3px lightgrey );
    filter: drop-shadow(1px 1px 3px rgb(17, 17, 17) );
  }

  .warehouse{
    margin-right: 50px;
  }

  .container {
    position: relative;
  }

  .image1 {
    opacity: 1;
    display: block;
    width: 250px;
    height: auto;
    transition: .5s ease;
    backface-visibility: hidden;
  }

  .middle {
    transition: .5s ease;
    opacity: 0;
    position: absolute;
    top: 80px;
    left: 140px;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    text-align: center;
  }

  .container:hover .image1 {
    opacity: 0.3;
  }

  .container:hover .middle {
    opacity: 1;
  }

  .middle:hover{
    cursor: pointer;
    color: blue ;
  }

  .data:hover{
    cursor: pointer;
    color:blue;
  }
</style>
