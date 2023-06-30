**Example 1: 开启加密数据保护**

开启加密数据保护

Input: 

```
tccli tke EnableEncryptionProtection --cli-unfold-argument  \
    --ClusterId cls-mu2or8b8 \
    --KMSConfiguration.KeyId 38098f4c-f5ef-11ed-8c28-525400b4ad52 \
    --KMSConfiguration.KmsRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "73779803-e28b-481a-a350-eab5bada499b"
    }
}
```

