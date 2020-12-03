**Example 1: 多经点位告警**



Input: 

```
tccli ump CreateMultiBizAlert --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --ZoneId 1 \
    --CameraId 1 \
    --CaptureTime 1600011956020 \
    --Image imagebase64stirng \
    --State 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

