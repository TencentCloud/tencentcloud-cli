**Example 1: 查询黑石路由表条目**



Input: 

```
tccli bmvpc DescribeRoutePolicies --cli-unfold-argument  \
    --RouteTableId rtb-afg8md3c \
    --RoutePolicyIds rti-q1j48dkd
```

Output: 
```
{
    "Response": {
        "RoutePolicySet": [
            {
                "RoutePolicyId": "Local",
                "RouteDescription": "",
                "DestinationCidrBlock": "Local",
                "GatewayType": "LOCAL",
                "GatewayId": "Local",
                "RoutePolicyType": "NETD",
                "Enabled": true
            },
            {
                "RoutePolicyId": "rti-q9eyoybe",
                "RouteDescription": "",
                "DestinationCidrBlock": "169.254.0.0/23",
                "GatewayType": "SSHSSLVPN",
                "GatewayId": "sslvpngw-o7tpr54i",
                "RoutePolicyType": "NETD",
                "Enabled": true
            }
        ],
        "TotalCount": 2,
        "RequestId": "62735da7-4546-4d63-8d42-36ced3bd3d94"
    }
}
```

