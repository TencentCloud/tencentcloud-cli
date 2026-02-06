**Example 1: 查询云原生网关访问控制**

查询云原生网关访问控制

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayIPRestriction --cli-unfold-argument  \
    --GatewayId gateway-2f2e3c40 \
    --SourceType route \
    --SourceId 31f3bf99-f289-4b6e-8edc-5e09d9d8ce4f
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d",
        "Result": {
            "SourceType": "route",
            "SourceId": "31f3bf99-f289-4b6e-8edc-5e09d9d8ce4f",
            "Enabled": true,
            "RestrictionType": "whiteList",
            "AddressList": [
                "1.1.1.1"
            ]
        }
    }
}
```

