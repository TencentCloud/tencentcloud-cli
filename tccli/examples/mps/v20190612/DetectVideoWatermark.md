**Example 1: 正常发起水印检测任务**



Input: 

```
tccli mps DetectVideoWatermark --cli-unfold-argument  \
    --InputInfo.Type URL \
    --InputInfo.UrlInputInfo.Url https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/ppeterhuang/yjcp_badcase_cut.mp4
```

Output: 
```
{
    "Response": {
        "Confidence": 98.33333333333333,
        "Description": "右下方有小红书Logo，左上方有“小红书”文字Logo，右上方有个人头像Logo，右上方有“喜老登”文字Logo。",
        "HasWatermark": true,
        "RequestId": "d02e3ed3-327f-42fc-9d34-c2e3ed8fba93"
    }
}
```

**Example 2: 正常发起水印检测任务带扩展**



Input: 

```
tccli mps DetectVideoWatermark --cli-unfold-argument  \
    --InputInfo.Type URL \
    --InputInfo.UrlInputInfo.Url https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/ppeterhuang/yjcp_badcase_cut.mp4 \
    --UserExtPara {"key": "value"}
```

Output: 
```
{
    "Response": {
        "Confidence": 99,
        "Description": "左下方有小红书Logo，右下方有小红书Logo，左上方有“小红书”台标，右上方有“喜老登”文字和用户头像。",
        "HasWatermark": true,
        "RequestId": "f94119bd-ab31-42c5-a445-16f9e8c7d741"
    }
}
```

