**Example 1: 设置中国大陆地区的日志投递目标**



Input: 

```
tccli vod SetCLSPushTarget --cli-unfold-argument  \
    --SubAppId 0 \
    --Domain abc.com \
    --ChineseMainlandCLSTargetInfo.Switch ON \
    --ChineseMainlandCLSTargetInfo.CLSRegion ap-guangzhou \
    --ChineseMainlandCLSTargetInfo.TopicId abc \
    --ChineseMainlandCLSTargetInfo.LogsetId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

