**Example 1: 查询示例**



Input: 

```
tccli waf DescribeOpUserSignaturePolicy --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1 \
    --Filters.0.Name AppId \
    --Filters.0.Values 251198060 \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Total": 1,
        "OpUserSigPolicy": [
            {
                "OpAppId": "050000000",
                "OpDomain": "xx.qcloudwaf.com",
                "Level": 300,
                "Status": 1,
                "ModifyTime": "2021-12-07T15:03:24+08:00"
            }
        ]
    }
}
```

