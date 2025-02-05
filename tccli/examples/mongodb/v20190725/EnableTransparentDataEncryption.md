**Example 1: 开启实例数据透明加密**



Input: 

```
tccli mongodb EnableTransparentDataEncryption --cli-unfold-argument  \
    --InstanceId cmgo-igjysqkr \
    --KmsRegion ap-guangzhou \
    --KeyId myEncryptionkey
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "RequestId": "a8dce7a4-d488-49c9-8d24-33cf623f5992"
    }
}
```

