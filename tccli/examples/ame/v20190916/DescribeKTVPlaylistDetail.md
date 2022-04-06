**Example 1: 获取即时广播歌单接口**

获取即时广播歌单接口

Input: 

```
tccli ame DescribeKTVPlaylistDetail --cli-unfold-argument  \
    --PlaylistId AME-201803241 \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "PlaylistBaseInfo": {
            "Description": "国内热门",
            "MusicNum": 1,
            "PlaylistId": "pid-xxfdds1",
            "Title": "国内热门"
        },
        "RequestId": "998d8d-11223-xxxd1-192j",
        "KTVMusicInfoSet": [
            {
                "ComposerSet": [
                    "方文山"
                ],
                "MusicId": "mid-xd998aa",
                "SingerSet": [
                    "周杰伦"
                ],
                "SingerInfoSet": [
                    {
                        "SingerId": "sid-19xjf8d",
                        "Name": "周杰伦"
                    }
                ],
                "TagSet": [
                    "情歌"
                ],
                "Duration": 241,
                "LyricistSet": [
                    "方文山"
                ],
                "Name": "七里香"
            }
        ]
    }
}
```

