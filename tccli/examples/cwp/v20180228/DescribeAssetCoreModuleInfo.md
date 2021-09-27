**Example 1: 获取内核模块详情**



Input: 

```
tccli cwp DescribeAssetCoreModuleInfo --cli-unfold-argument  \
    --Quuid xx \
    --Uuid xx \
    --Id xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Module": {
            "Processes": "xx",
            "Name": "xx",
            "Modules": "xx",
            "UpdateTime": "xx",
            "Version": "xx",
            "Params": [
                {
                    "Data": "xx",
                    "Name": "xx"
                }
            ],
            "Path": "xx",
            "Desc": "xx",
            "Size": 1
        }
    }
}
```

