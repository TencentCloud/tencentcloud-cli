**Example 1: 更新实例外网白名单**



Input: 

```
tccli tcr ModifySecurityPolicy --cli-unfold-argument  \
    --RegistryId tcr-test123 \
    --CidrBlock 192.168.0.0/24 \
    --Description test \
    --PolicyIndex 1
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

