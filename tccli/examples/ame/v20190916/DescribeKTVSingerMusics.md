**Example 1: 获取歌手下歌曲列表**

获取歌手下歌曲列表

Input: 

```
tccli ame DescribeKTVSingerMusics --cli-unfold-argument  \
    --SingerId xx \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
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
        ],
        "RequestId": "xx"
    }
}
```

