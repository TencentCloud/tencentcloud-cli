**Example 1: 开启实例数据透明加密**



Input: 

```
tccli mongodb EnableTransparentDataEncryption --cli-unfold-argument  \
    --InstanceId cmgo-igjysqkr \
    --KmsRegion ap-guangzhou \
    --KeyId abcabc
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "RequestId": "abcd"
    }
}
```

