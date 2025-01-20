**Example 1: 根据公网ip查询云原生网关实例信息**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayInfoByIp --cli-unfold-argument  \
    --PublicNetworkIP 1.1.1.1
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "gateway-a1337ce3",
            "GroupId": "group-a1337ce"
        },
        "RequestId": "86e4eecf-51a5-4dda-9cec-68650a9b8c3b"
    }
}
```

