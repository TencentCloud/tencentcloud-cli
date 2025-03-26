**Example 1: 设置中国大陆地区的日志投递目标**



Input: 

```
tccli vod SetCLSPushTarget --cli-unfold-argument  \
    --SubAppId 0 \
    --Domain abc.com \
    --ChineseMainlandCLSTargetInfo.Switch ON \
    --ChineseMainlandCLSTargetInfo.CLSRegion ap-guangzhou \
    --ChineseMainlandCLSTargetInfo.TopicId topic***001 \
    --ChineseMainlandCLSTargetInfo.LogsetId logset***001
```

Output: 
```
{
    "Response": {
        "RequestId": "2dsew***d2a"
    }
}
```

