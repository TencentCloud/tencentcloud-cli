**Example 1: 获取歌曲伴奏链接**

获取歌曲伴奏链接

Input: 

```
tccli yinsuda DescribeKTVMusicAccompanySegmentUrl --cli-unfold-argument  \
    --AppName abc \
    --UserId abc \
    --MusicId abc \
    --PlayScene abc \
    --RoomId abc
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Url": "abc",
        "ExtName": "abc",
        "SegmentBegin": 0,
        "SegmentEnd": 0,
        "FileSize": 0,
        "OtherSegments": [
            {
                "SegmentBegin": 0,
                "SegmentEnd": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 获取歌曲伴奏链接(脱敏)**

脱敏的实际请求

Input: 

```
tccli yinsuda DescribeKTVMusicAccompanySegmentUrl --cli-unfold-argument  \
    --AppName monk_dev \
    --UserId monk \
    --MusicId mid-9Eyb67xe
```

Output: 
```
{
    "Response": {
        "ExtName": "mkv",
        "FileSize": 1087189,
        "OtherSegments": [
            {
                "SegmentBegin": 91798,
                "SegmentEnd": 120177
            }
        ],
        "RequestId": "865e06ab-1aae-42e1-ae29-3137f143fb01",
        "SegmentBegin": 91798,
        "SegmentEnd": 120177,
        "Status": 0,
        "Url": "http://****/202306151716/****/0db8f1208ee298295cc6c81bac448751"
    }
}
```

