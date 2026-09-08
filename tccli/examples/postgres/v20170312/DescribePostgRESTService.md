**Example 1: 查询PostgREST服务详情信息**



Input: 

```
tccli postgres DescribePostgRESTService --cli-unfold-argument  \
    --DBInstanceId postgres-0uwjmh8t
```

Output: 
```
{
    "Response": {
        "CreateTime": "2026-05-11 15:15:50",
        "JWTSecret": "dsfadlsfjkadsjfalkdfjads",
        "NetworkAccessList": [
            {
                "Address": "",
                "Ip": "10.0.0.7",
                "NetType": "private",
                "Port": 3000,
                "ProtocolType": "postgrest",
                "Status": "opened",
                "SubnetId": "subnet-3hekhnki",
                "VpcId": "vpc-a27ykb0r"
            }
        ],
        "Status": "running",
        "RequestId": "2066fe70-ca9d-4b1d-8c6d-76ac834251cf"
    }
}
```

