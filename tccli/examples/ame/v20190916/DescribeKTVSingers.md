**Example 1: 获取直播互动曲库歌手**



Input: 

```
tccli ame DescribeKTVSingers --cli-unfold-argument  \
    --Sort.Field xx \
    --Sort.Order xx \
    --Limit 0 \
    --Offset 0 \
    --Genders MALE \
    --SingerIds xx \
    --Areas CH
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "KTVSingerInfoSet": [
            {
                "SingerId": "xx",
                "Name": "xx",
                "Area": "xx",
                "Gender": "xx",
                "PlayCount": 10,
                "MusicCount": 10
            }
        ],
        "RequestId": "xx"
    }
}
```

