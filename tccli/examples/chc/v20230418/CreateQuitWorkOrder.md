**Example 1: 创建设备退出工单**



Input: 

```
tccli chc CreateQuitWorkOrder --cli-unfold-argument  \
    --IdcId 2005 \
    --DeviceType server \
    --StuffOption 2 \
    --IsPowerOffConfirm 1 \
    --DeviceSnList lihwli021718420010 \
    --HandoverMethod 2 \
    --CustomerReceipt.PickUpStuff 张三 \
    --CustomerReceipt.PickUpStuffContact 15311111111 \
    --CustomerReceipt.PickUpStuffIDCard 100000000000000005 \
    --CustomerReceipt.PickUpTime 2025-03-08 12:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "ece01139-3175-4f9e-8c15-3a513839c405",
        "WorkOrderSet": [
            {
                "OrderType": "powerOff",
                "ServiceType": "quit",
                "WorkOrderId": "ord-25030714282926976"
            },
            {
                "OrderType": "rackOff",
                "ServiceType": "quit",
                "WorkOrderId": "ord-25030714282967608"
            },
            {
                "OrderType": "quit",
                "ServiceType": "quit",
                "WorkOrderId": "ord-25030714282957052"
            },
            {
                "OrderType": "personnelVisit",
                "ServiceType": "quit",
                "WorkOrderId": "ord-25030714282880371"
            }
        ]
    }
}
```

