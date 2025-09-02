**Example 1: 上报订单信息**

用于用户上报自定义的订单信息，多网聚合加速服务将相关信息进行保存

Input: 

```
tccli mna ReportOrder --cli-unfold-argument  \
    --OrderId 100003848 \
    --ProjectId 4002428 \
    --PackageType pack_1 \
    --ReportMonth 2025-08
```

Output: 
```
{
    "Response": {
        "RequestId": "3f00ee83-0ce6-4148-86c5-e3e3dc44920b",
        "OrderInfo": {
            "OrderId": "100003848",
            "ProjectId": "4002428",
            "PackageType": "pack_1",
            "ReportMonth": "2025-08"
        }
    }
}
```

