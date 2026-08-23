**Example 1: 查询镜像仓库列表**



Input: 

```
tccli csip DescribeImageRegistryList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "ImageRegistryList": [
            {
                "ConnDetectDetail": [
                    {
                        "ConnDetectMessage": "",
                        "ConnDetectStatus": "status_connecting",
                        "FailReason": "",
                        "Quuid": "backend",
                        "Solution": "",
                        "Uuid": "backend"
                    }
                ],
                "InstanceID": "",
                "Name": "ccr-default",
                "RegistryId": 5,
                "RegistryRegion": "default",
                "RegistryType": "ccr",
                "RegistryVersion": "",
                "SyncMode": 0,
                "Url": "https://ccr.ccs.tencentyun.com"
            }
        ],
        "TotalCount": 2,
        "RequestId": "45694c4e-008c-4fae-9c64-bcba5a91062a"
    }
}
```

