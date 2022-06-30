**Example 1: 获取源站组详情**



Input: 

```
tccli teo DescribeOriginGroupDetail --cli-unfold-argument  \
    --OriginId origin-xxx \
    --ZoneId zone-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "OriginId": "origin-136db381-8d3d-11ec-89a4-00ff977fb3c8",
        "OriginName": "oname",
        "ZoneId": "zone-xxx",
        "ZoneName": "123.com",
        "Record": [
            {
                "Area": [],
                "Port": 10,
                "Record": "1.2.3.4",
                "RecordId": "record-4b2dbd84-8d9a-11ec-9527-00ff977fb3c8",
                "Weight": 100
            }
        ],
        "Type": "weight",
        "OriginType": "self",
        "ApplicationProxyUsed": false,
        "LoadBalancingUsed": false,
        "LoadBalancingUsedType": "none",
        "UpdateTime": "2020-09-22T00:00:00+00:00"
    }
}
```

