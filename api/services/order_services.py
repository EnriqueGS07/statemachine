from ..repositories import order_repository
from ..models.order_model import Order
from rest_framework.exceptions import NotFound
from django.utils import timezone
import random

POSIBLE_TRANSITIONS = {
"Pending": {"pendingBiometricalVerification":"OnHold","noVerificationNeeded":"PendingPayment","orderCancelled":"Cancelled","paymentFailed":"Cancelled","orderCancelledByUser":"Cancelled"},
"OnHold":{"biometricalVerificationSuccessful":"PendingPayment","orderCancelledByUser":"Cancelled","verificationFailed":"Cancelled" },
"PendingPayment":{"paymentSuccessful":"Confirmed","orderCancelledByUser":"Cancelled"},
"Confirmed":{"preparingShipment":"Processing","orderCancelledByUser":"Cancelled" },
"Processing":{"itemDispatched":"Shipped","orderCancelledByUser":"Cancelled" },
"Shipped":{"itemReceivedByCustomer":"Delivered","deliveryIssue":"OnHold","orderCancelledByUser":"Cancelled"},
"Delivered":{"Returning":"returnInitiatedByCustomer"},
"Returning":{"returnInitiatedByCustomer":"Returned","orderCancelledByUser": "Cancelled"},
"Returned":{"refundProcessed":"Refunded"},
"Refunded":{},
"Cancelled":{}
}

def generate_unique_ticket():
    while True:
        ticket = random.randint(10000, 99999)  # Puedes ajustar el rango si necesitas más combinaciones
        if not Order.objects.filter(active_ticket=ticket).exists():
            return ticket

#ORDERS
def list_orders():
    return order_repository.get_all_orders()

def create_order_service(data):
    if "user" not in data :
        raise ValueError("La orden debe tener un usuario")
    if data["amount"] > 1000:
        print("Se genero ticket")
        data["active_ticket"] = generate_unique_ticket()
    return order_repository.create_order(data)

def get_order_by_id(order_id):
    try:
        return Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        None
        
def delete_order_service(pk):
    try:
        order = Order.objects.get(pk=pk)
        order.delete()
    except Order.DoesNotExist:
        raise NotFound()

def delete_all_orders_service():
    return order_repository.delete_all_orders()

def get_new_state(current_state, trigger):
    posible_actions = POSIBLE_TRANSITIONS[current_state]
    if trigger not in posible_actions.keys():
        return None 
    else:
        return posible_actions[trigger]

def update_log(pk, trigger):
    order = Order.objects.filter(id=pk).first()
    if not order:
        raise ValueError("Orden no encontrada")
    
    new_state = get_new_state(order.current_state, trigger)
    if not new_state:
        raise ValueError("No se pudo actualizar el log de estados")
    
    time = timezone.now().isoformat()
    order.state_log.append({new_state:{"evento": trigger, "hora": time}})
    order.current_state = new_state
    order.save()
    return order

