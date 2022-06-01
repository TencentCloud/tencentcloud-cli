**Example 1: 获取负载均衡详细信息**



Input: 

```
tccli teo DescribeLoadBalancingDetail --cli-unfold-argument  \
    --ZoneId zone-xxx \
    --LoadBalancingId lb-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
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
}
```

