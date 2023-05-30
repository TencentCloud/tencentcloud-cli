**Example 1: 删除实例公网访问白名单策略**

删除实例公网访问白名单

Input: 

```
tccli tcr DeleteSecurityPolicy --cli-unfold-argument  \
    --RegistryId tcr-test123 \
    --PolicyIndex 1 \
    --PolicyVersion 1 \
    --CidrBlock 0.0.0.0/20
```

Output: 
```
{
    "Response": {
        "RegistryId": "tcr-test123",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

