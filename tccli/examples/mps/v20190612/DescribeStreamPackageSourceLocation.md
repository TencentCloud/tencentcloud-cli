**Example 1: 请求示例**

查询媒体包装SourceLocation信息。

Input: 

```
tccli mps DescribeStreamPackageSourceLocation --cli-unfold-argument  \
    --Id 66503E8E0000930000F0
```

Output: 
```
{
    "Response": {
        "Info": {
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
        },
        "RequestId": "req-xxx"
    }
}
```

