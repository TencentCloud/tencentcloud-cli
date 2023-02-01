**Example 1: Waf IP黑白名单Delete接口**

删除IP黑白名单

Input: 

```
tccli waf DeleteIpAccessControl --cli-unfold-argument  \
    --Domain test.qcloudwaf.com \
    --Items 1.2.3.4 \
    --DeleteAll False
```

Output: 
```
{
    "Response": {
        "FailedCount": 0,
        "FailedItems": "",
        "RequestId": "9fbb7be2-214b-44df-a5b9-6a69ca456409"
    }
}
```

