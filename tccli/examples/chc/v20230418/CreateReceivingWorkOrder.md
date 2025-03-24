**Example 1: 创建设备收货工单**



Input: 

```
tccli chc CreateReceivingWorkOrder --cli-unfold-argument  \
    --IdcId 159 \
    --DeviceType server \
    --EntryTime 2025-03-08 00:00:00 \
    --ReceivingOperation 1 \
    --IsExpressDelivery False \
    --ServerDeviceList.0.DeviceSn chc20250308xxx001 \
    --ServerDeviceList.0.ModelVersion DELL R740-T1-V1
```

Output: 
```
{
    "Response": {
        "RequestId": "e1006a5c-4a9f-463e-963a-7f6ba01edffe",
        "WorkOrderSet": [
            {
                "OrderType": "receiving",
                "ServiceType": "receiving",
                "WorkOrderId": "ord-25030711283032499"
            }
        ]
    }
}
```

