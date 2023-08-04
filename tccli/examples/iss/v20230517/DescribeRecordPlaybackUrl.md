**Example 1: 成功**

 

Input: 

```
tccli iss DescribeRecordPlaybackUrl --cli-unfold-argument  \
    --ChannelId 32525dd7-c3fc-****-****-d5beb4acd1e1 \
    --StartTime 1687677795 \
    --EndTime 1687688595
```

Output: 
```
{
    "Response": {
        "Data": {
            "Hls": "https://test5.maxshang.cn/playback/32525dd7-c3fc-****-****-d5beb4acd1e1/hls.m3u8?starttime=1687677795&endtime=1687688595&token=13*******2_1687677842_68dfc39854510520f29de4da78bd6e93"
        },
        "RequestId": "ba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

