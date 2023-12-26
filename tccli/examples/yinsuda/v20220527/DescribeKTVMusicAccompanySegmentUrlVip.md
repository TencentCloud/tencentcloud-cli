**Example 1: 获取歌曲伴奏片段链接（会员）**

获取歌曲伴奏片段链接（会员）

Input: 

```
tccli yinsuda DescribeKTVMusicAccompanySegmentUrlVip --cli-unfold-argument  \
    --AppName Mtest \
    --UserId James \
    --MusicId mid-GHJAIQP
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
        "RequestId": "abc"
    }
}
```

