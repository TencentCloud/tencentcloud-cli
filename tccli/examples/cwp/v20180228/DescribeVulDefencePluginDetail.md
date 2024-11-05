**Example 1: 获取单台主机漏洞防御插件信息**



Input: 

```
tccli cwp DescribeVulDefencePluginDetail --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Quuid f3076bef-0fdf-44f4-bb63-b5232e13e167 \
    --Filters.0.Name Status \
    --Filters.0.Values 1 \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Pid": 28942,
                "MainClass": "org.apache.catalina.startup.Bootstrap",
                "Status": 1,
                "ErrorLog": "error",
                "InjectLog": "failed"
            }
        ],
        "RequestId": "de9c0927-3177-48f5-9212-2c3354a4c011",
        "TotalCount": 1
    }
}
```

