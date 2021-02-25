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
    --State 1 \
    --Warnings.0.Id -1 \
    --Warnings.0.MonitoringArea.0.X 0 \
    --Warnings.0.MonitoringArea.0.Y 0 \
    --Warnings.0.MonitoringArea.1.X 1920 \
    --Warnings.0.MonitoringArea.1.Y 0 \
    --Warnings.0.MonitoringArea.2.X 1920 \
    --Warnings.0.MonitoringArea.2.Y 1080 \
    --Warnings.0.MonitoringArea.3.X 0 \
    --Warnings.0.MonitoringArea.3.Y 1080 \
    --Warnings.0.WarningInfos.0.WarningType 1 \
    --Warnings.0.WarningInfos.0.WarningAreaSize 100 \
    --Warnings.0.WarningInfos.0.WarningLocation.X 100 \
    --Warnings.0.WarningInfos.0.WarningLocation.Y 100 \
    --Warnings.0.WarningInfos.0.WarningAreaContour.0.X 100 \
    --Warnings.0.WarningInfos.0.WarningAreaContour.0.Y 100
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

