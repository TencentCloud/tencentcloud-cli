**Example 1: 访问资产**



Input: 

```
tccli dasb AccessDevice --cli-unfold-argument  \
    --ResourceId bh-saas-xxxxxxxx \
    --InstanceId ins-xxxxxxxx \
    --Account root \
    --Password  \
    --PrivateKey  \
    --PrivateKeyPassword  \
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

