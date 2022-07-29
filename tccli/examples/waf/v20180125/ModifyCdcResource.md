**Example 1: ModifyCdcResource**



Input: 

```
tccli waf ModifyCdcResource --cli-unfold-argument  \
    --Id 0 \
    --OpAppId 1 \
    --ClusterId 1 \
    --Ip 192.168.1.1 \
    --Port 6379 \
    --Auth passwd \
    --Type redis \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

