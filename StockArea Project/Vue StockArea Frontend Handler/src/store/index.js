import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    warehouse_list : []
  },
  getters:{
    warehouse_list: (state) => state.warehouse_list
  },
  mutations: {
  },
  actions: {
    fetch_data(){
      Vue.axios.get('http://127.0.0.1:9000/ajax/get_warehouse_data')
      .then(resp => {
        this.state.warehouse_list = resp.data
      })
    },
    edit_data({commit},val){
      console.log(commit)
      console.log(val)
      for(let i =0; i < this.state.warehouse_list.length;i++){
        if(this.state.warehouse_list[i].id == val.id){
          this.state.warehouse_list[i] = val
        }
      }
      console.log(this.state.warehouse_list)
    }
  },
  modules: {
  }
})
