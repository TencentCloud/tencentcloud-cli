**Example 1: 获取指定站点的负载均衡列表**



Input: 

```
tccli teo DescribeLoadBalancing --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name zone-id \
    --Filters.0.Values zone-20hzkd4rdmy0 \
    --Filters.0.Fuzzy False
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "TotalCount": 1,
        "Data": [
            {
                "Host": "test.tencent.com",
                "LoadBalancingId": "lb-d21bfaf7-8d72-11ec-841d-00ff977fb3c8",
                "OriginGroupId": "orgin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a",
                "BackupOriginGroupId": "",
                "TTL": 600,
                "Type": "proxied",
                "UpdateTime": "2022-02-14T08:48:03Z",
                "ZoneId": "zone-20hzkd4rdmy0",
                "Status": "online",
                "Cname": "test.tencent.com.acc.edgeonedy1.com",
                "OriginType": "normal",
                "AdvancedOriginGroups": []
            }
        ]
    }
}
```

**Example 2: 获取指定ID的负载均衡信息**



Input: 

```
tccli teo DescribeLoadBalancing --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name zone-id \
    --Filters.0.Values zone-20hzkd4rdmy0 \
    --Filters.0.Fuzzy False \
    --Filters.1.Name load-balancing-id \
    --Filters.1.Values lb-d21bfaf7-8d72-11ec-841d-00ff977fb3c8 \
    --Filters.1.Fuzzy False
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "TotalCount": 1,
        "Data": [
            {
                "Host": "test.tencent.com",
                "LoadBalancingId": "lb-d21bfaf7-8d72-11ec-841d-00ff977fb3c8",
                "OriginGroupId": "orgin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a",
                "BackupOriginGroupId": "",
                "TTL": 600,
                "Type": "proxied",
                "UpdateTime": "2022-02-14T08:48:03Z",
                "ZoneId": "zone-20hzkd4rdmy0",
                "Status": "online",
                "Cname": "test.tencent.com.acc.edgeonedy1.com",
                "OriginType": "normal",
                "AdvancedOriginGroups": []
            }
        ]
    }
}
```

**Example 3: 获取指定域名的负载均衡信息（模糊查询）**



Input: 

```
tccli teo DescribeLoadBalancing --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name zone-id \
    --Filters.0.Values zone-20hzkd4rdmy0 \
    --Filters.0.Fuzzy False \
    --Filters.1.Name host \
    --Filters.1.Values test \
    --Filters.1.Fuzzy True
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "TotalCount": 1,
        "Data": [
            {
                "Host": "test.tencent.com",
                "LoadBalancingId": "lb-d21bfaf7-8d72-11ec-841d-00ff977fb3c8",
                "OriginGroupId": "orgin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a",
                "BackupOriginGroupId": "",
                "TTL": 600,
                "Type": "proxied",
                "UpdateTime": "2022-02-14T08:48:03Z",
                "ZoneId": "zone-20hzkd4rdmy0",
                "Status": "online",
                "Cname": "test.tencent.com.acc.edgeonedy1.com",
                "OriginType": "normal",
                "AdvancedOriginGroups": []
            }
        ]
    }
}
```

