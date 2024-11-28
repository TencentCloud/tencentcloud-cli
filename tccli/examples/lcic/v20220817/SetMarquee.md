**Example 1: 设置跑马灯参数设置**



Input: 

```
tccli lcic SetMarquee --cli-unfold-argument  \
    --SdkAppId 34442819 \
    --RoomId 353861 \
    --MarqueeType 1 \
    --DisplayMode 1 \
    --Content #FFFF00 \
    --FontSize 11 \
    --FontWeight 1 \
    --FontOpacity 0.3 \
    --BackgroundColor #FFFF00 \
    --BackgroundOpacity 0.3 \
    --Duration 3 \
    --MarqueeCount 1
```

Output: 
```
{
    "Response": {
        "RequestId": "87c8dcd3-5941-4920-a7b6-bcdc13af7c79"
    }
}
```

