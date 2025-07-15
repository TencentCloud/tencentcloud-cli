**Example 1: 查询多通道安全加速网关列表**

查询多通道安全加速网关列表，一页显示 10 行记录，不带过滤条件。

Input: 

```
tccli teo DescribeMultiPathGateways --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Gateways": [
            {
                "GatewayId": "mpgw-lbxuhk1oh",
                "GatewayName": "mpgw",
                "GatewayType": "private",
                "GatewayPort": 8080,
                "Status": "online",
                "GatewayIP": "101.43.204.125"
            }
        ],
        "RequestId": "a622678d-ea5b-41e8-9cd2-d335816141a0",
        "TotalCount": 1
    }
}
```

