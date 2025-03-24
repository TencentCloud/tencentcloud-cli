**Example 1: 创建设备下架工单**



Input: 

```
tccli chc CreateRackOffWorkOrder --cli-unfold-argument  \
    --IdcId 2005 \
    --DeviceType server \
    --StuffOption 2 \
    --IsPowerOffConfirm 1 \
    --DeviceSnList lihwli021718420012
```

Output: 
```
{
    "Response": {
        "RequestId": "5b09296a-8e17-4033-846e-79acaf3bc809",
        "WorkOrderSet": [
            {
                "OrderType": "powerOff",
                "ServiceType": "rackOff",
                "WorkOrderId": "ord-25030714251078382"
            },
            {
                "OrderType": "rackOff",
                "ServiceType": "rackOff",
                "WorkOrderId": "ord-25030714251022115"
            }
        ]
    }
}
```

