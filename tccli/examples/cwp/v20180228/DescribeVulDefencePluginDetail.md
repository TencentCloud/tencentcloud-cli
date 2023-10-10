**Example 1: 获取单台主机漏洞防御插件信息**



Input: 

```
tccli cwp DescribeVulDefencePluginDetail --cli-unfold-argument  \
    --Quuid d92d723e-4aac-4f4a-bbf9-e5430e29d289
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": 0,
                "MainClass": "xx",
                "ErrorLog": "xx",
                "Pid": 0,
                "InjectLog": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

