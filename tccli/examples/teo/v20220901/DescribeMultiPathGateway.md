**Example 1: 查询云上网关详情**

查询站点 ID 为 zone-27q0p0bal192 下，网关 ID 为 mpgw-9d65563y6p 的详细信息。

Input: 

```
tccli teo DescribeMultiPathGateway --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-9d65563y6p
```

Output: 
```
{
    "Response": {
        "GatewayDetail": {
            "GatewayId": "mpgw-9d65563y6p",
            "GatewayIP": "49.233.240.134",
            "GatewayName": "EOMPGW-1",
            "GatewayPort": 8080,
            "RegionId": "ap-beijing",
            "Status": "online",
            "GatewayType": "cloud",
            "Lines": [
                {
                    "LineAddress": "49.233.240.134:8080",
                    "LineId": "line-0",
                    "LineType": "direct"
                }
            ]
        },
        "RequestId": "aaab53cb-23c4-4b13-85f5-e63745107ba0"
    }
}
```

**Example 2: 查询自有网关详情**

查询站点 ID 为 zone-27q0p0bal192 下，网关 ID 为 mpgw-9d6asd63376 的详细信息。

Input: 

```
tccli teo DescribeMultiPathGateway --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-9d6asd63376
```

Output: 
```
{
    "Response": {
        "GatewayDetail": {
            "GatewayId": "mpgw-9d6asd63376",
            "GatewayIP": "41.125.20.114",
            "GatewayName": "EOMPGW-2",
            "GatewayPort": 8080,
            "RegionId": "ap-shanghai",
            "Status": "online",
            "GatewayType": "private",
            "Lines": [
                {
                    "LineAddress": "43.213.14.191:8080",
                    "LineId": "line-0",
                    "LineType": "direct"
                }
            ]
        },
        "RequestId": "aaab53cb-23c4-4b13-85f5-e63745107ba0"
    }
}
```

