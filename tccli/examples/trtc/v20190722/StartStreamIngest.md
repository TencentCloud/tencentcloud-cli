**Example 1: 开启在线输入媒体流**



Input: 

```
tccli trtc StartStreamIngest --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --RoomId 9988101 \
    --RoomIdType 1 \
    --UserId u46618234 \
    --UserSig eJw1jUsOgkAQBa9CZm1wej4Nmrjwu1AxEeQABAZsDTgBNBrj3RXFbb1UvSc7bCO3oYKNHabaeb6ZJRhcpo94EZkwPYFcjfLQrOUSStof092wqGxsgwkbOF-V3C3V5mOD1lpwznveZOfEWsq6RXEOvi8R**1m6u5OuPxfaan8NjxE5YHQ0HPKTNVSTj-hqhDBF1Kx1xv7mTKR \
    --StreamUrl https://webrtc-backup-record-default-1258344699.cos.ap-nanjing.myqcloud.com/runningwang/output_f100040.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "b4096f81-8633-4475-9ee1-8ce4eab20849",
        "TaskId": "CR6LqvF7KfFBEyRihlxDN5RBXjdLDEn-LZgRFr+rTEL2p6vnZV4vRaRm5zJS3tEiSir0mwHw-Y5itMY+Rcfy3QpDMCzfXWl5CXXrEFRHuOGHxJCzqSY."
    }
}
```

