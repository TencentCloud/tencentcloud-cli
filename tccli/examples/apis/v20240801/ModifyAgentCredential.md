**Example 1: 修改Credential**

修改Credential

Input: 

```
tccli apis ModifyAgentCredential --cli-unfold-argument  \
    --InstanceID ins-e6fbc9b9 \
    --ID agc-f4431972 \
    --Name 测试 \
    --Type reqKey \
    --Content.STSSystem  \
    --Content.STSService  \
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
        "RequestId": "0cd7d9e9-5eb8-456d-b50d-747c5b236ef8"
    }
}
```

