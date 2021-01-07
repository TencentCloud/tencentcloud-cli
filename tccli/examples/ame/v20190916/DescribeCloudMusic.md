**Example 1: 获取云音乐播放信息**

获取云音乐播放信息

Input: 

```
tccli ame DescribeCloudMusic --cli-unfold-argument  \
    --MusicId xxx
```

Output: 
```
{
    "Response": {
        "Duration": 288,
        "MusicId": "xxx",
        "MusicImageUrl": "http://xxx.com/album/097/976740-JPG-240X240-ALBUM.jpg",
        "MusicName": "低温xx",
        "MusicUrl": "https://xxx.com/wm/10/384/10384721-MP3-128K-FTW-P.mp3?sign=4d7428e523c0d419e6c05db5912c8c67&t=5fcf112a&transDeliveryCode=CA@0@1607400466@S@c56ea136420f5044",
        "RequestId": "s1607400465431774000",
        "Singers": [
            "陈xx"
        ]
    }
}
```

