**Example 1: Disabling a Connection**



Input: 

```
tccli gaap CloseProxies --cli-unfold-argument  \
    --ProxyIds link-11112222
```

Output: 
```
{
    "Response": {
        "OperationFailedInstanceSet": [],
        "RequestId": "888fe1bb-be58-4a80-90b9-24a0398633c6",
        "InvalidStatusInstanceSet": []
    }
}
```

