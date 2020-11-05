**Example 1: Terminating a Connection**



Input: 

```
tccli gaap DestroyProxies --cli-unfold-argument  \
    --ProxyIds link-11112222 link-11113333\
    --Force 1
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

