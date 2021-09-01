**Example 1: 获取分类内容下歌曲列表**



Input: 

```
tccli ame DescribeItems --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --CategoryId xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Items": [
            {
                "ItemID": "xx",
                "Album": {
                    "ImagePathMap": [
                        {
                            "Value": "xx",
                            "Key": "xx"
                        },
                        {
                            "Key": "xx",
                            "Value": "xx"
                        },
                        {
                            "Key": "xx",
                            "Value": "xx"
                        },
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "AlbumName": "xx"
                },
                "Status": 0,
                "DataInfo": {
                    "Duration": "xx",
                    "AuditionBegin": 1,
                    "Version": "xx",
                    "Name": "xx",
                    "AuditionEnd": 1
                },
                "Artists": [
                    {
                        "ArtistName": "xx"
                    }
                ]
            }
        ],
        "HaveMore": 1,
        "Offset": 1,
        "Total": 1,
        "Size": 1
    }
}
```

