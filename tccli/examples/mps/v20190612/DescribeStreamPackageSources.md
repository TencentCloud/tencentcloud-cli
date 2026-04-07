**Example 1: 请求示例**

查询Source信息列表。

Input: 

```
tccli mps DescribeStreamPackageSources --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 1 \
    --LocationId 66503E8E0000930000F0 \
    --Type VOD
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Name": "source_name",
                "Type": "VOD",
                "PackageConf": [
                    {
                        "GroupName": "group_name",
                        "Type": "HLS",
                        "Path": "/vod/demo.m3u8"
                    }
                ],
                "Id": "66503E8E0000930000F1",
                "CreateTime": 1590508800,
                "UpdateTime": 1590508800,
                "Region": "ap-singapore"
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

