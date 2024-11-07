**Example 1: 访问资产**



Input: 

```
tccli dasb AccessDevice --cli-unfold-argument  \
    --ResourceId bh-saas-1a2b3d \
    --InstanceId ins-1a2b3d \
    --Account root \
    --Password pwd \
    --PrivateKey test-key \
    --PrivateKeyPassword test-key-pwd \
    --Protocol SSH
```

Output: 
```
{
    "Response": {
        "AccessInfo": {
            "Ip": "127.0.0.1",
            "Port": "80",
            "User": "root@xxxx",
            "Password": ""
        },
        "RequestId": "77d99ae2-8c7f-484c-b1d6-fe45df130fc0"
    }
}
```

