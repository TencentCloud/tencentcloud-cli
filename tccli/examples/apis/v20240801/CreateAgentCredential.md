**Example 1: 创建Credential**

创建Credential

Input: 

```
tccli apis CreateAgentCredential --cli-unfold-argument  \
    --InstanceID ins-e6fbc9b9 \
    --Name 测试凭据 \
    --Type reqKey \
    --Content.Headers.0.Key x-rio-signature \
    --Content.Headers.0.Value 123456789
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "agc-f4431972"
        },
        "RequestId": "70f5a87e-91d0-4b6a-8720-efd5f3ccec9e"
    }
}
```

