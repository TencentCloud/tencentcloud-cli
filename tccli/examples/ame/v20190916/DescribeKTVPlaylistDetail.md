**Example 1: 获取即时广播歌单接口**

获取即时广播歌单接口

Input: 

```
tccli ame DescribeKTVPlaylistDetail --cli-unfold-argument  \
    --PlaylistId xx \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "PlaylistBaseInfo": {
            "Description": "xx",
            "MusicNum": 0,
            "PlaylistId": "xx",
            "Title": "xx"
        },
        "RequestId": "xx",
        "KTVMusicInfoSet": [
            {
                "ComposerSet": [
                    "xx"
                ],
                "MusicId": "xx",
                "SingerSet": [
                    "xx"
                ],
                "TagSet": [
                    "xx"
                ],
                "Duration": 1,
                "LyricistSet": [
                    "xx"
                ],
                "Name": "xx"
            }
        ]
    }
}
```

