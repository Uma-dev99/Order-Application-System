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

# Endpoints of Django App "Orders"

The following are the available endpoints for the "Orders" app:

```python
urlpatterns = [
    path('ofv/', views.orderFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>/', views.updateView, name='update_url'),
    path('del/<int:f_oid>/', views.deleteView, name='delete_url'),
]


## Results:

![Screenshot 2024-10-15 010405](https://github.com/user-attachments/assets/f1d390a2-8a87-4c02-a0de-de2bb027e206)
![Screenshot 2024-10-15 010255](https://github.com/user-attachments/assets/62aa4ab9-ce81-4a2e-82fb-9c474c4cb46c)
