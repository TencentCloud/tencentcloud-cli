**Example 1: 获取歌手下歌曲列表**

获取歌手下歌曲列表

Input: 

```
tccli ame DescribeKTVSingerMusics --cli-unfold-argument  \
    --SingerId sid-38xhhdd0 \
    --Limit 10 \
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
                    "方文山"
                ],
                "MusicId": "mid-399x9e91",
                "SingerSet": [
                    "周杰伦"
                ],
                "SingerInfoSet": [
                    {
                        "SingerId": "sid-38xhhdd0",
                        "Name": "周杰伦"
                    }
                ],
                "TagSet": [
                    "伤感"
                ],
                "Duration": 241,
                "LyricistSet": [
                    "方文山"
                ],
                "Name": "七里香"
            }
        ],
        "RequestId": "c163a5b7-b4c9-4b71-9202-81532d9c69dc"
    }
}
```

