**Example 1: 查询网关版本信息接口实例**

根据网关ID查询版本信息

Input: 

```
tccli tcb DescribeGatewayVersions --cli-unfold-argument  \
    --EnvId env-test-xxx \
    --GatewayId gw-002
```

Output: 
```
{
    "Response": {
        "GatewayId": "gw-xxx",
        "TotalCount": 1,
        "GatewayVersionItems": [
            {
                "VersionName": "versionName-xxx",
                "Weight": 100
            }
        ],
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

