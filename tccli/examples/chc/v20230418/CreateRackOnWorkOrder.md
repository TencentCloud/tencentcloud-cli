**Example 1: 创建设备上架工单**



Input: 

```
tccli chc CreateRackOnWorkOrder --cli-unfold-argument  \
    --IdcId 373 \
    --DeviceType server \
    --StuffOption 2 \
    --WithPowerOn False \
    --DeviceRackOnList.0.DeviceSn lihwli10225021 \
    --DeviceRackOnList.0.DstRackName M302-J01 \
    --DeviceRackOnList.0.DstPositionCode 7
```

Output: 
```
{
    "Response": {
        "RequestId": "4fd6eff1-2613-48dd-be51-a74ac082ff34",
        "WorkOrderSet": [
            {
                "OrderType": "rackOn",
                "ServiceType": "rackOn",
                "WorkOrderId": "ord-25030711311423914"
            }
        ]
    }
}
```

