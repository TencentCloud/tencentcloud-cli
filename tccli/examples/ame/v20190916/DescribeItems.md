**Example 1: 获取分类内容下歌曲列表**



Input: 

```
tccli ame DescribeItems --cli-unfold-argument  \
    --Limit 1\
    --Offset 0\
    --CategoryId xxxxx
```

Output: 
```
{
    "Response": {
        "HaveMore": 4,
        "Items": [
            {
                "Album": {
                    "AlbumName": "一个人喝醉",
                    "ImagePathMap": [
                        {
                            "Key": "JPG-240X240-ALBUM",
                            "Value": "http://xxx.com/album/094/941465-JPG-240X240-ALBUM.jpg"
                        },
                        {
                            "Key": "JPG-320X320-ALBUM",
                            "Value": "http://xxx.com/album/094/941465-JPG-320X320-ALBUM.jpg"
                        },
                        {
                            "Key": "JPG-600X600-ALBUM",
                            "Value": "http://xxx.com/album/094/941465-JPG-600X600-ALBUM.jpg"
                        },
                        {
                            "Key": "JPG-1000X1000-ALBUM",
                            "Value": "http://xxx.com/album/094/941465-JPG-1000X1000-ALBUM.jpg"
                        }
                    ]
                },
                "Artists": [
                    {
                        "ArtistName": "刘增瞳"
                    }
                ],
                "DataInfo": {
                    "AuditionBegin": 52000,
                    "AuditionEnd": 83000,
                    "Duration": "00:03:41",
                    "Name": "一个人喝醉",
                    "Version": ""
                },
                "ItemID": "6A48A96A0253EBF45569BB40AF7AEF00"
            }
        ],
        "Offset": 0,
        "RequestId": "s1568790504896049000",
        "Size": 1,
        "Total": 5
    }
}
```

