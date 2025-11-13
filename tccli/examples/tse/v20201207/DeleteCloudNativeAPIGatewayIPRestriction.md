**Example 1: 删除云原生网关访问控制**

删除云原生网关访问控制

Input: 

```
tccli tse DeleteCloudNativeAPIGatewayIPRestriction --cli-unfold-argument  \
    --GatewayId gateway-2f2e3c42 \
    --SourceType route \
    --SourceId 31f3bf99-f289-4b6e-8edc-5e09d9d8ce4e
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

