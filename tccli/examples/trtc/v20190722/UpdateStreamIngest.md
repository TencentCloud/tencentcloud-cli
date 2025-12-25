**Example 1: 更新输入在线媒体流**



Input: 

```
tccli trtc UpdateStreamIngest --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --TaskId CR6LqvF7KfFBEyRihlxDN5RBXjdLDEn-LZgRFr+rTEL2p6vnZV4vRaRm5zJS3tEiSir0mwHw-Y5itMY+Rcfy3QpDMCzfXWl5CXXrEFRHuOGHxJCzqSY. \
    --StreamUrl https://webrtc-backup-record-default-1258344699.cos.ap-nanjing.myqcloud.com/runningwang/48d0c7e46f088ee97208f0815ddc8b20.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "b070fb8a-0fa2-4a3c-8675-0756e014770b",
        "Status": "InProgress"
    }
}
```

