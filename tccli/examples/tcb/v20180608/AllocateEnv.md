**Example 1: 从环境池里分配1个环境**



Input: 

```
tccli tcb AllocateEnv --cli-unfold-argument  \
    --AllocateId m****************3 \
    --ExternalAppId appid********* \
    --ExternalTag tab********sion=PR***TE
```

Output: 
```
{
    "Response": {
        "EnvId": "******-d8gx4e0pr5de21d1c",
        "ExternalAppId": "appid*********",
        "RequestId": "633be6a9-049a-4a88-a111-e78be09d58bc"
    }
}
```

