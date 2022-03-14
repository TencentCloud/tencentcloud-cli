**Example 1: 获取直播互动曲库歌手**



Input: 

```
tccli ame DescribeKTVSingers --cli-unfold-argument  \
    --Sort.Field PlayCount \
    --Sort.Order Desc \
    --Limit 1 \
    --Offset 0 \
    --Genders MALE \
    --Areas CH
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "KTVSingerInfoSet": [
            {
                "SingerId": "sid-8h3h3gs",
                "Name": "周杰伦",
                "Area": "港台",
                "Gender": "男",
                "PlayCount": 10,
                "MusicCount": 10
            }
        ],
        "RequestId": "2hs73j3-2fur9j4-3jke44-hdhh2"
    }
}
```

