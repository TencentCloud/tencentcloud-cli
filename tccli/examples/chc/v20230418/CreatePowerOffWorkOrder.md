**Example 1: 创建设备关电工单**



Input: 

```
tccli chc CreatePowerOffWorkOrder --cli-unfold-argument  \
    --IdcId 2005 \
    --DeviceType server \
    --IsPowerOffConfirm 1 \
    --DeviceSnList lihwli02130003
```

Output: 
```
{
    "Response": {
        "RequestId": "f60e609f-eaa9-43c2-ba21-fcbc9e321efe",
        "WorkOrderSet": [
            {
                "OrderType": "powerOff",
                "ServiceType": "powerOff",
                "WorkOrderId": "ord-25030714181161269"
            }
        ]
    }
}
```

