**Example 1: 修改实例公网IP白名单配置**

修改实例公网IP白名单配置

Input: 

```
tccli ckafka ModifyAccessPolicy --cli-unfold-argument  \
    --InstanceId ckafka-ay3z77qe \
    --RouteId 137946 \
    --IpWhitelist.0.CidrBlock 127.0.0.1 \
    --IpWhitelist.0.PolicyDescription test-description
```

Output: 
```
{
    "Response": {
        "Result": "Succeed",
        "RequestId": "0ca44380-3c17-4755-9564-f48de2e01760"
    }
}
```

