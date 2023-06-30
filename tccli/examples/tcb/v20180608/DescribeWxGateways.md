**Example 1: 查看容器托管的所有服务**



Input: 

```
tccli tcb DescribeWxGateways --cli-unfold-argument  \
    --EnvId lotestapi100004
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Gateways": [
            {
                "Status": "xx",
                "L5Addr": "xx",
                "EnvId": "xx",
                "GatewayName": "xx",
                "AllowUncertified": 0,
                "SubnetIds": [
                    "xx"
                ],
                "UpdateTime": "xx",
                "GatewayDesc": "xx",
                "Uin": "xx",
                "ExpireTime": "xx",
                "GatewayType": "xx",
                "IsolateTime": "xx",
                "VpcId": "xx",
                "PackageId": 1,
                "AppId": 1,
                "GatewayId": "xx",
                "PackageVersion": "xx",
                "CreateTime": "xx",
                "Region": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

