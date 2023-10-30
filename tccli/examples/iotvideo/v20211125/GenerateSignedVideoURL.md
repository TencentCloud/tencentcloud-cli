**Example 1: 获取视频防盗链播放URL**



Input: 

```
tccli iotvideo GenerateSignedVideoURL --cli-unfold-argument  \
    --ExpireTime 1619331648 \
    --VideoURL http://zylcb.iotvideo.tencentcs.com/timeshift/live/1.m3u8
```

Output: 
```
{
    "Response": {
        "SignedVideoURL": "http://zylcb.iotvideo.tencentcs.com/timeshift/live/1.m3u8?sign=x",
        "RequestId": "abc"
    }
}
```

