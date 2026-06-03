**Example 1: 请求示例**

查询SourceLocation信息列表。

Input: 

```
tccli mps DescribeStreamPackageSourceLocations --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Id": "66503E8E0000930000F0",
                "Name": "location_name",
                "Region": "ap-singapore",
                "BaseUrl": "https://base.com/",
                "SegmentDeliverEnable": true,
                "SegmentDeliverConf": {
                    "DefaultSegmentUrl": "https://base.com/demo/",
                    "NameServers": [
                        {
                            "Name": "server_name",
                            "Url": "https://test.com/"
                        }
                    ]
                },
                "AttachedLiveSources": [
                    "66503E8E0000930000F2"
                ],
                "AttachedVodSources": [
                    "66503E8E0000930000F1"
                ],
                "CreateTime": 1590508800,
                "UpdateTime": 1590508800,
                "SegmentDeliverUsePackageEnable": true
            }
        ],
        "PageNum": 1,
        "PageSize": 1,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "req-xxx"
    }
}
```

