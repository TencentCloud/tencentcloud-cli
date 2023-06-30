**Example 1: 删除网关某版本接口示例**

根据网关ID和版本名称删除版本

Input: 

```
tccli tcb DeleteGatewayVersion --cli-unfold-argument  \
    --EnvId env-test-xxx \
    --GatewayId gw-002 \
    --VersionName gw-002-001
```

Output: 
```
{
    "Response": {
        "Result": "success",
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

