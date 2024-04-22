**Example 1: ResetAccountPassword**



Input: 

```
tccli sqlserver ResetInstancePassword --cli-unfold-argument  \
    --UserAppId 0 \
    --UserResourceId abc \
    --ResourceRegion abc \
    --ResourceAccount abc \
    --Password abc \
    --AccountHost abc
```

Output: 
```
{
    "Response": {
        "TimeCost": 0,
        "ResetTimestamp": 0,
        "RequestId": "abc"
    }
}
```

