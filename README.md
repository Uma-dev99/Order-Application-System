# Order-Application-System
## Features 
Developed Order Application  System using HTML , CSS , JavaScript and Django in Backend which performs CRUD Operations.
Made use of Sqlite DB using Models (MVT architecture - Model, View , template)
Utilised Django Forms 

## List of APIs created 

1. OrderFormView 
2. ShowView
3. UpdateView
4. DeleteView

## Endpoints of Django App "Orders"
'''
urlpatterns = [
    path('ofv/', views.orderFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name= 'update_url'),
    path('del/<int:f_oid>', views.deleteView, name= 'delete_url'),
]

'''
## Results:

![Screenshot](assets/img/Screenshot 2024-10-15 010255.png)