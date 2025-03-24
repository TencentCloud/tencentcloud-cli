**Example 1: 提交服务器类型的通用服务工单**



Input: 

```
tccli chc CreateCommonServiceWorkOrder --cli-unfold-argument  \
    --DevicePositionSet.0.Sn 217404176 \
    --DevicePositionSet.0.RackName M203-B14 \
    --DevicePositionSet.0.IdcUnitId 2555 \
    --DevicePositionSet.0.PositionCode 1 \
    --ServiceLevel 1 \
    --PreAuthorization True \
    --ContactName 张三 \
    --ContactPhone 13800138000 \
    --DeviceType server \
    --Instructions test
```

Output: 
```
{
    "Response": {
        "RequestId": "7600c206-c7c2-40f8-bea8-195a2efa8c7a",
        "WorkOrderSet": [
            {
                "OrderType": "itCommon",
                "ServiceType": "serverCommon",
                "WorkOrderId": "ord-25030711115960582"
            }
        ]
    }
}
```

