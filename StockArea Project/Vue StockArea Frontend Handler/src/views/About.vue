<template>
  <div class="bg-info" style="padding:30px; display:flex; height:100%">
    <img src="@/images.jpg" class="image">
    <svg @click="edit()" class="edit" xmlns="http://www.w3.org/2000/svg" width="23"         height="23" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.66V20a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h5.34"></path><polygon points="18 2 22 6 12 16 8 16 8 12 18 2"></polygon></svg>
    <div id="myModal" class="modal">
      <div class="modal-content" >
        <h3>Edit details</h3>    
        <p style="display:flex;">City:
          <input type="text" class="updated_input" v-model="current_warehouse[0].city">
        </p>
        <p style="display:flex;">Cluster:
          <input type="text" class="updated_input" v-model="current_warehouse[0].cluster">
        </p>
        <p style="display:flex;">Space Available:
          <input type="text" class="updated_input" v-model="current_warehouse[0].space_available">
        </p>
        <p style="display:flex;">Code:
          <input type="text" class="updated_input" v-model="current_warehouse[0].code">
        </p>
        <p style="display:flex;">Type:
          <input type="text" class="updated_input" v-model="current_warehouse[0].type">
        </p>
        <p style="display:flex;">Registered:
          <input type="text" class="updated_input" v-model="current_warehouse[0].is_registered">
        </p>
        <p style="display:flex;">Live:
          <input type="text" class="updated_input" v-model="current_warehouse[0].is_live">
        </p>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="save_warehouse_changes">Save changes</button>
          <button type="button" class="btn btn-secondary" @click="close_modal()">Close</button>
        </div>
      </div>
    </div>
    <div class="text-white" style="margin-left:auto; margin-right:auto">
      <h1 class="text-dark">{{current_warehouse[0].name}}</h1>
      <div style="display:flex"> 
        <h3 class="head">City:</h3>
        <h3 class="text">{{current_warehouse[0].city}}</h3>
      </div>
      <div style="display:flex"> 
        <h3 class="head">Cluster:</h3>
        <h3 class="text">{{current_warehouse[0].cluster}}</h3>
      </div>
      <div style="display:flex"> 
        <h3 class="head">Space Available:</h3>
        <h3 class="text">{{current_warehouse[0].space_available}}</h3>
      </div>  
      <div style="display:flex"> 
        <h3 class="head">Code:</h3>
        <h3 class="text">{{current_warehouse[0].code}}</h3>
      </div>  
      <div style="display:flex"> 
        <h3 class="head">Type:</h3>
        <h3 class="text">{{current_warehouse[0].type}}</h3>
      </div>  
      <div style="display:flex"> 
        <h3 class="head">Registered:</h3>
        <h3 class="text">{{current_warehouse[0].is_registered}}</h3>
      </div>  
      <div style="display:flex"> 
        <h3 class="head">Live:</h3>
        <h3 class="text">{{current_warehouse[0].is_live}}</h3>
      </div>  
      
    </div>
  </div>
</template>

<script>
import { mapGetters,mapActions } from 'vuex'

export default {
  name: 'About',
  created(){
    console.log(this.current_warehouse)
  },
  methods:{
    ...mapActions(['edit_data']),
    edit(){
      var modal = document.getElementById("myModal");
      modal.style.display = "block"; 
    },

    close_modal(){
      var modal = document.getElementById("myModal");
      modal.style.display = "none"; 
    },

    save_warehouse_changes(){
      this.edit_data(this.current_warehouse[0])
      this.close_modal()
    }
  },
  
  computed:{
    ...mapGetters(['warehouse_list']),
    current_warehouse(){
      return this.warehouse_list.filter(warehouse => warehouse.id ==this.$route.params.id)
    }
  }

}
</script>

<style >
 .image {
    display: flex;
    margin: 20px;
    width: 500px;
  }

  .head{
    position:relative; 
    right:80px;
  }

  .text{
    position:absolute; 
    right:270px;
  }

  .edit{
    position: absolute;
    margin-top:10px;
    right:100px
  }

  .edit:hover{
    color: aliceblue;
  }

  .modal{
    position: fixed;
    z-index: 1; 
    width: 100%;
    height: 100%; 
    overflow-y:scroll; 
    background-color: rgb(0,0,0); 
    background-color: rgba(0, 0, 0, 0.2);
  }

  .modal-content {
    background-color: #fefefe;
    margin: 10% auto; 
    padding: 20px;
    overflow-y:auto; 
    max-width: 50%; 
  } 

  .updated_input{
    width: 200px;
    border: 2px solid black;
    position: relative;
    left:20px;
  }
</style> 