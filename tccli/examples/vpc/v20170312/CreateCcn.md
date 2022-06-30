**Example 1: 创建一个CCN**



Input: 

```
tccli vpc CreateCcn --cli-unfold-argument  \
    --CcnDescription test+description \
    --Tags.0.Value shanghai \
    --Tags.0.Key city \
    --CcnName test+name \
    --QosLevel PT
```

Output: 
```
{
    "Response": {
        "Ccn": {
            "CcnId": "ccn-gjug0kul",
            "CcnName": "test name",
            "RoutePriorityFlag": false,
            "CcnDescription": "test description",
            "InstanceCount": 0,
            "QosLevel": "PT",
            "State": 1,
            "InstanceChargeType": "POSTPAID",
            "BandwidthLimitType": "OUTER_REGION_LIMIT",
            "CreateTime": "2020-09-22 00:00:00",
            "RouteTableFlag": null,
            "RouteTableCount": null,
            "TagSet": [
                {
                    "Key": "city",
                    "Value": "shanghai"
                }
            ]
        },
        "RequestId": "b8351d12-3c82-4d4b-9d88-972e02ca4620"
    }
}
```

