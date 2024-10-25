**Example 1: 获取内核模块详情**



Input: 

```
tccli cwp DescribeAssetCoreModuleInfo --cli-unfold-argument  \
    --Quuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Uuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Id 1024
```

Output: 
```
{
    "Response": {
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82",
        "Module": {
            "Processes": "sshd",
            "Name": "test-name",
            "Modules": "ssh",
            "UpdateTime": "2024-10-11 12:23:34",
            "Version": "0.1.1",
            "Params": [
                {
                    "Data": "",
                    "Name": "test-name"
                }
            ],
            "Path": "/root",
            "Desc": "",
            "Size": 1
        }
    }
}
```

