**Example 1: 请求示例**

查询媒体包装Source信息。

Input: 

```
tccli mps DescribeStreamPackageSource --cli-unfold-argument  \
    --Id 66503E8E0000930000F1
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
            "Id": "66503E8E0000930000F1",
            "CreateTime": 1590508800,
            "UpdateTime": 1590508800,
            "Region": "ap-singapore"
        },
        "RequestId": "req-xxx"
    }
}
```

