**Example 1: 获取应用密钥**



Input: 

```
tccli lke GetAppSecret --cli-unfold-argument  \
    --LoginUin 700000963993 \
    --LoginSubAccountUin 700000963993 \
    --AppBizId 1801166480814637056
```

Output: 
```
{
    "Response": {
        "AppKey": "HuLJbSdLZ",
        "CreateTime": "1718266528",
        "IsRelease": false,
        "HasPermission": true,
        "RequestId": "ee325589-ef62-4aab-8070-01792336d02a"
    }
}
```

