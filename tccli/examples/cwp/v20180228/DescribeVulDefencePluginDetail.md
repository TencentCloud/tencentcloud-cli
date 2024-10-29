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
                "Pid": 2302060,
                "MainClass": "org.springframework.boot.loader.JarLauncher",
                "Status": 1,
                "ErrorLog": "",
                "InjectLog": ""
            }
        ],
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

