**Example 1: 获取直播互动曲库歌曲的周榜和月榜**

获取直播互动曲库歌曲的周榜和月榜

Input: 

```
tccli ame DescribeKTVTopList --cli-unfold-argument  \
    --Type Hot \
    --Period Week
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "KTVMusicTopInfoSet": [
            {
                "ComposerSet": [
                    "xx"
                ],
                "SingerInfoSet": [
                    {
                        "SingerId": "xx",
                        "Name": "xx"
                    }
                ],
                "MusicId": "xx",
                "TagSet": [
                    "xx"
                ],
                "Duration": 0,
                "LyricistSet": [
                    "xx"
                ],
                "Name": "xx"
            }
        ]
    }
}
```

