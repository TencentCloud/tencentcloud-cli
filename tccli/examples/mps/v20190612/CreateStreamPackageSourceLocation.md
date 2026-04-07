**Example 1: 请求示例**

创建媒体包装频道。

Input: 

```
tccli mps CreateStreamPackageSourceLocation --cli-unfold-argument  \
    --Name location_name \
    --BaseUrl https://base.com/ \
    --SegmentDeliverEnable True \
    --SegmentDeliverConf.DefaultSegmentUrl https://base.com/demo/ \
    --SegmentDeliverConf.NameServers.0.Name server_name \
    --SegmentDeliverConf.NameServers.0.Url https://test.com/ \
    --SegmentDeliverUsePackageEnable True
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

