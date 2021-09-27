**Example 1: 获取资产管理Web框架列表**



Input: 

```
tccli cwp DescribeAssetWebFrameList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "WebFrames": [
            {
                "OsInfo": "xx",
                "Lang": "xx",
                "ServiceType": "xx",
                "MachineWanIp": "xx",
                "Uuid": "xx",
                "ProjectId": 1,
                "Tag": [
                    {
                        "TagId": 1,
                        "Rid": 0,
                        "Name": "xx"
                    }
                ],
                "Version": "xx",
                "Quuid": "xx",
                "MachineName": "xx",
                "MachineIp": "xx",
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

