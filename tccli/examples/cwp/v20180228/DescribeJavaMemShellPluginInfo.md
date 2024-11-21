**Example 1: 查询给定主机java内存马插件信息**



Input: 

```
tccli cwp DescribeJavaMemShellPluginInfo --cli-unfold-argument  \
    --Quuid 05f0bcab-726c-4ea4-8109-bcd03d5598f7 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "d92d723e-4aac-4f4a-bbf9-e5430e29d289",
        "TotalCount": 1,
        "List": [
            {
                "Pid": 21756,
                "MainClass": "main.class",
                "Status": 1,
                "ErrorLog": "[INFO]libpath..."
            }
        ]
    }
}
```

