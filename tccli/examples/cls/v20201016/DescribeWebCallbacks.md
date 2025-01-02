**Example 1: 获取告警渠道回调配置列表**

获取告警渠道回调配置列表

Input: 

```
tccli cls DescribeWebCallbacks --cli-unfold-argument  \
    --Filters.0.Key name \
    --Filters.0.Values 监控告警专用 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "WebCallbacks": [
            {
                "WebCallbackId": "webcallback-285a1bef-xxxx-xxxx-b6b3-6fd9326d6876",
                "Name": "监控告警专用",
                "Type": "WeCom",
                "Webhook": "http://www.xxx.com",
                "Method": "POST",
                "Uin": 100001000000,
                "SubUin": 100021900000,
                "CreateTime": 1705998110,
                "UpdateTime": 1705998110
            }
        ],
        "TotalCount": 1,
        "RequestId": "d20a21f7-xxxx-xxxx-ba1b-1aa49be5fed1"
    }
}
```

