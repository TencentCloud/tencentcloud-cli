**Example 1: 根据歌曲ID查询歌曲信息**



Input: 

```
tccli ame DescribeItemById --cli-unfold-argument  \
    --ItemIDs xxx
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Album": {
                    "AlbumName": "你像她",
                    "ImagePathMap": [
                        {
                            "Key": "JPG-240X240-ALBUM",
                            "Value": "http://image.tingmall.com/album/172/1727096-JPG-240X240-ALBUM.jpg"
                        },
                        {
                            "Key": "JPG-320X320-ALBUM",
                            "Value": "http://image.tingmall.com/album/172/1727096-JPG-320X320-ALBUM.jpg"
                        },
                        {
                            "Key": "JPG-600X600-ALBUM",
                            "Value": "http://image.tingmall.com/album/172/1727096-JPG-600X600-ALBUM.jpg"
                        },
                        {
                            "Key": "JPG-1000X1000-ALBUM",
                            "Value": "http://image.tingmall.com/album/172/1727096-JPG-1000X1000-ALBUM.jpg"
                        }
                    ]
                },
                "Artists": [
                    {
                        "ArtistName": "炫青"
                    }
                ],
                "DataInfo": {
                    "AuditionBegin": 31000,
                    "AuditionEnd": 58000,
                    "Duration": "00:04:25",
                    "Name": "你像她",
                    "Version": "伴奏"
                },
                "ItemID": "58E772961AA8DD0D5569BB40AF7AEF08"
            }
        ],
        "RequestId": "s1590115749573388000"
    }
}
```

