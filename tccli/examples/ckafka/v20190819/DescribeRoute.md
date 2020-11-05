**Example 1: Viewing route information**



Input: 

```
tccli ckafka DescribeRoute --cli-unfold-argument  \
    --InstanceId xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Routers": [
                {
                    "AccessType": 0,
                    "RouteId": 2,
                    "VipType": 4,
                    "VipList": [
                        {
                            "Vip": "9.13.100.63",
                            "Vport": "8774"
                        }
                    ]
                }
            ]
        },
        "RequestId": "e36d80f9-21aa-4a22-9932-91e1fbd12f39"
    }
}
```

