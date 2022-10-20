**Example 1: 查询漏洞防御插件列表**



Input: 

```
tccli tcss DescribeVulDefencePlugin --cli-unfold-argument  \
    --HostID xx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": "xx",
                "MainClass": "xx",
                "ErrorLog": "xx",
                "PID": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

