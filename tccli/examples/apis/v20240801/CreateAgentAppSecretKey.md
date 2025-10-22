**Example 1: 创建app的secretKey**

创建app的secretKey

Input: 

```
tccli apis CreateAgentAppSecretKey --cli-unfold-argument  \
    --InstanceID ins-9c4a1db3 \
    --ID test
```

Output: 
```
{
    "Response": {
        "Data": {
            "SecretID": "AK51a1185e86E4E5B10c6e3c8fB4EDF5A8",
            "SecretKey": "a7d93ae078A04DF35bd2c84e490DDB72"
        },
        "RequestId": "fe886567-b0f7-47f0-81a8-4b990ce09492"
    }
}
```

