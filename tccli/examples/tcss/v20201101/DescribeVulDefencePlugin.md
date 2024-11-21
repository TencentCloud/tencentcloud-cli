**Example 1: 查询漏洞防御插件列表**

查询漏洞防御插件列表

Input: 

```
tccli tcss DescribeVulDefencePlugin --cli-unfold-argument  \
    --HostID 3b6b1bbc-1c7a-47e2-9ca8-e9c27ec9d068 \
    --Limit 1 \
    --Offset 1 \
    --Filters.0.Name Status \
    --Filters.0.Values SUCCESS \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "PID": 0,
                "MainClass": "com.java.main",
                "Status": "SUCCESS",
                "ErrorLog": ""
            }
        ],
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

