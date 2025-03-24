**Example 1: 创建设备搬迁工单**



Input: 

```
tccli chc CreateMovingWorkOrder --cli-unfold-argument  \
    --IdcId 373 \
    --DeviceType server \
    --WithPowerOn False \
    --DeviceMovingList.0.DeviceSn LD-SERVER-20250124-002 \
    --DeviceMovingList.0.DstRackName M302-J01 \
    --DeviceMovingList.0.DstPositionCode 20
```

Output: 
```
{
    "Response": {
        "RequestId": "bd5139d4-b3fa-41ef-bf7a-9e8166975903",
        "WorkOrderSet": [
            {
                "OrderType": "rackOff",
                "ServiceType": "moving",
                "WorkOrderId": "ord-25030714334568923"
            },
            {
                "OrderType": "rackOn",
                "ServiceType": "moving",
                "WorkOrderId": "ord-25030714334565831"
            }
        ]
    }
}
```

