from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    warehouse_list = [
      {
        'id':1, 
        'name':'Warehouse-165', 
        'code':'W-00001', 
        'city':'Delhi', 
        'space_available':'1234', 
        'type':'Leasable Space', 
        'cluster':'cluster-a-32', 
        'is_registered':'True', 
        'is_live':'False'
      },
      {
        'id':2, 
        'name':'Warehouse-276', 
        'code':'W-00002', 
        'city':'Chennai', 
        'space_available':'124', 
        'type':'Warehouse Service', 
        'cluster':'cluster-a-1', 
        'is_registered':'True', 
        'is_live':'False'
      },
      {
        'id':3, 
        'name':'Warehouse-3039', 
        'code':'W-00003', 
        'city':'Indore', 
        'space_available':'134', 
        'type':'Warehouse Service', 
        'cluster':'cluster-a-1', 
        'is_registered':'True', 
        'is_live':'False'
      },
      {
        'id':4, 
        'name':'Warehouse-324', 
        'code':'W-00004', 
        'city':'Chennai', 
        'space_available':'12', 
        'type':'Leasable Space', 
        'cluster':'cluster-a-21', 
        'is_registered':'True', 
        'is_live':'False'
      },
      {
        'id':5, 
        'name':'Warehouse-5454', 
        'code':'W-00005', 
        'city':'Chennai', 
        'space_available':'1243434', 
        'type':'Warehouse Service', 
        'cluster':'cluster-a-21', 
        'is_registered':'True', 
        'is_live':'False'
      },
      {
        'id':6, 
        'name':'Warehouse-4345', 
        'code':'W-00006', 
        'city':'Chennai', 
        'space_available':'1', 
        'type':'Leasable Space', 
        'cluster':'cluster-a-21', 
        'is_registered':'True', 
        'is_live':'False'
      },
      {
        'id':7, 
        'name':'Warehouse-3455', 
        'code':'W-00007', 
        'city':'Mumbai', 
        'space_available':'4', 
        'type':'Leasable Space', 
        'cluster':'cluster-a-2', 
        'is_registered':'True', 
        'is_live':'False'
      },
      {
        'id':8, 
        'name':'Warehouse-23455', 
        'code':'W-00008', 
        'city':'Banglore', 
        'space_available':'3456', 
        'type':'Warehouse Service', 
        'cluster':'cluster-a-21', 
        'is_registered':'True', 
        'is_live':'False'
      },
    ]
    return JsonResponse(warehouse_list, safe=False)
