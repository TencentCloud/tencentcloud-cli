**Example 1: 查询漏洞防御插件列表**

查询漏洞防御插件列表

Input: 

```
tccli tcss DescribeVulDefencePlugin --cli-unfold-argument  \
    --HostID abc \
    --Limit 1 \
    --Offset 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
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
                "MainClass": "abc",
                "Status": "abc",
                "ErrorLog": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

