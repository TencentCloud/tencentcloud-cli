**Example 1: 获取私有域解析概览**



Input: 

```
tccli privatedns DescribeDashboard --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "3c979890-0dcf-917e-d7a696c04d429009",
        "ZoneTotal": 20,
        "ZoneVpcCount": 7,
        "RequestTotalCount": 10000,
        "FlowUsage": [
            {
                "FlowType": "zone",
                "TotalQuantity": 20,
                "AvailableQuantity": 20
            },
            {
                "FlowType": "traffic",
                "TotalQuantity": 2000000,
                "AvailableQuantity": 2000000
            }
        ]
    }
}
```

