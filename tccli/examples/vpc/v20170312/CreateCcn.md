**Example 1: Creating a CCN**



Input: 

```
tccli vpc CreateCcn --cli-unfold-argument  \
    --CcnName test+name\
    --CcnDescription test+description\
    --QosLevel PT\
    --Tags.0.Key city\
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "Ccn": {
            "CcnId": "ccn-gjug0kul",
            "CcnName": "test name",
            "CcnDescription": "test description",
            "InstanceCount": 0,
            "CreatedTime": "0000-00-00 00:00:00",
            "QosLevel": "PT",
            "InstanceChargeType": "POSTPAID",
            "BandwidthLimitType": "OUTER_REGION_LIMIT",
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

