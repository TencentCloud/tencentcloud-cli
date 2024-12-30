**Example 1: 获取告警渠道回调配置列表**

获取告警渠道回调配置列表

Input: 

```
tccli cls DescribeWebCallbacks --cli-unfold-argument  \
    --Filters.0.Key name \
    --Filters.0.Values test \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "WebCallbacks": [
            {
                "WebCallbackId": "webcallback-d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1",
                "Type": "Http",
                "Webhook": "http://www.xxx.com",
                "Method": "POST",
                "Key": "",
                "CreateTime": 1693468888,
                "UpdateTime": 1693468888
            }
        ],
        "TotalCount": 1,
        "RequestId": "d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1"
    }
}
```

