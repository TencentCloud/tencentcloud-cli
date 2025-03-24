**Example 1: 创建设备开电工单**



Input: 

```
tccli chc CreatePowerOnWorkOrder --cli-unfold-argument  \
    --IdcId 373 \
    --DeviceType server \
    --DeviceSnList TEN948P04K
```

Output: 
```
{
    "Response": {
        "RequestId": "18a2463c-d31c-4125-8d28-7c5f018e7440",
        "WorkOrderSet": [
            {
                "OrderType": "powerOn",
                "ServiceType": "powerOn",
                "WorkOrderId": "ord-25030711320087815"
            }
        ]
    }
}
```

