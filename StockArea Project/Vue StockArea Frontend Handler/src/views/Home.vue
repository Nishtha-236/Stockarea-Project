<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <img class="navbar-brand" src="@/logo.png" style="margin-top:-5px;">
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav" style="margin-top:1px">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
          <div class="input-group rounded">
            <input type="text" class="form-control rounded" v-model="search_text" placeholder="Search by name" aria-label="Search" aria-describedby="search-addon" />
            <span class="input-group-text border-0" id="search-addon">
              <img class="icon" src="@/Icon map-search.svg"/>
            </span>
          </div>
          <mdb-dropdown class="filter">
            <mdb-dropdown-toggle slot="toggle">Filter by</mdb-dropdown-toggle>
            <mdb-dropdown-menu>
              <mdb-dropdown-item @click="selected_filter('city')">City</mdb-dropdown-item>
              <mdb-dropdown-item @click="selected_filter('cluster')">Cluster</mdb-dropdown-item>
              <mdb-dropdown-item @click="selected_filter('space_available')">Space Available</mdb-dropdown-item>
            </mdb-dropdown-menu>
          </mdb-dropdown>
          <div v-if="selected_filter_display" style="display:flex;background-color: turquoise;border: none;border-radius: 20px;">
            <h4 style="color: white;font-size: 20px;margin: 6px 0px; padding: 2px 10px; ">
            {{selected_filter_display}}
            </h4>
            <svg @click="clear_filter()" class="clear" style="margin: 11px 5px;" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </div>
        </ul>
      </div>
    </nav>
    <div v-for="warehouse in filteredPosts" :key="warehouse.id">
      <HelloWorld :warehouse = "warehouse"/>
    </div>
  </div>
</template>

<script>
import { mdbDropdown, mdbDropdownItem, mdbDropdownMenu, mdbDropdownToggle } from 'mdbvue';
import HelloWorld from '@/components/HelloWorld.vue'
import { mapGetters} from 'vuex'



export default {
  name: 'Home',
  components: {
    HelloWorld,
    mdbDropdown,
    mdbDropdownItem,
    mdbDropdownMenu,
    mdbDropdownToggle
  },

  data() {
    return {
      search_text : "",
      selected_filter_display: null,
      selected: false,
      temp_warehouse_list : null,
    }
  },

  methods: {
    selected_filter(val){
      console.log(this.selected)
      this.selected_filter_display = val
      this.temp_warehouse_list = this.warehouse_list.sort( (a,b)=>{
          if(a[this.selected_filter_display]<b[this.selected_filter_display]){
            return -1
          }
          else if(a[this.selected_filter_display]>b[this.selected_filter_display]){
            return 1
          }
          else{
            return 0
          }
        })
      this.selected = !this.selected
      console.log(this.selected)
    },
    clear_filter(){
      this.selected_filter_display = null
    }
  },

  computed: {
    ...mapGetters(['warehouse_list']),
    filteredPosts(){
      if(this.selected_filter_display){
        return this.temp_warehouse_list
      }
      else{
        return this.warehouse_list.filter(warehouse => warehouse.name.toLowerCase().includes(this.search_text.toLowerCase())||warehouse.city.toLowerCase().includes(this.search_text.toLowerCase()) )
      }
    }
  },

  mounted(){
  }
  
}
</script>

<style>

  input{
    border: none;
    margin-left: 820px;
    width: 100%;
    height: 100%;
  }
  .icon{
    width: 14px;
    position: absolute;
    right:5px;
  }
  .icon:hover{
    cursor: pointer;
  }

  .filter{
    display: flex;
    border: none;
    margin-top: 2px;
    height: 33px;
    opacity: 1;
    width: 130px;
    margin-left: 15px;
  }

  .nav-item:hover{
    cursor: pointer;
    color: white;
    background-color:  rgb(71, 71, 71);
  }

  dropdown-toggle{
    position: absolute;
    margin-left: 55px;
    margin-top: -3px;
  }

  .clear:hover{
    color: aliceblue;
  }

</style>