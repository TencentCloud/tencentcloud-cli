**Example 1: 获取负载均衡列表**



Input: 

```
tccli teo DescribeLoadBalancing --cli-unfold-argument  \
    --ZoneId zone-xxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TotalCount": 10,
        "Data": [
            {
                "Host": "host",
                "LoadBalancingId": "lb-d21bfaf7-8d72-11ec-841d-00ff977fb3c8",
                "Origin": [],
                "OriginId": [],
                "TTL": 123,
                "Type": "type",
                "UpdateTime": "2022-02-14T08:48:03Z",
                "ZoneId": "zid",
                "Status": "online",
                "Cname": "1.2.3.4.com"
            }
        ]
    }
}
```

