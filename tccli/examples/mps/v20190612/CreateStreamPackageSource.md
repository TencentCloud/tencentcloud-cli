**Example 1: 请求示例**

创建媒体包装频道。

Input: 

```
tccli mps CreateStreamPackageSource --cli-unfold-argument  \
    --AttachedLocation 66503E8E0000930000F0 \
    --Name source_name \
    --Type VOD \
    --PackageConfs.0.GroupName group_name \
    --PackageConfs.0.Type HLS \
    --PackageConfs.0.Path /vod/main.m3u8
```

Output: 
```
{
    "Response": {
        "Info": {
            "Name": "source_name",
            "Type": "VOD",
            "PackageConf": [
                {
                    "GroupName": "group_name",
                    "Type": "HLS",
                    "Path": "/vod/main.m3u8"
                }
            ],
            "Id": "66503E8E0000930000F0",
            "CreateTime": 1590508800,
            "UpdateTime": 1590508800,
            "Region": "ap-singapore"
        },
        "RequestId": "req-xxx"
    }
}
```

