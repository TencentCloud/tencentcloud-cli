**Example 1: 销毁通道**



Input: 

```
tccli gaap DestroyProxies --cli-unfold-argument  \
    --Force 1 \
    --ProxyIds link-11113333 link-11112222
```

Output: 
```
{
    "Response": {
        "OperationFailedInstanceSet": [],
        "RequestId": "d4228b1a-8b3b-43d6-a8e7-272d158ff332",
        "InvalidStatusInstanceSet": [
            "link-11112222"
        ]
    }
}
```

