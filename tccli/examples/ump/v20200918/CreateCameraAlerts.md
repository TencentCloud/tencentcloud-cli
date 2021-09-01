**Example 1: 上报相机移动、遮挡等告警信息**



Input: 

```
tccli ump CreateCameraAlerts --cli-unfold-argument  \
    --Alerts.0.GroupCode group_code \
    --Alerts.0.MallId 1 \
    --Alerts.0.CameraId 1 \
    --Alerts.0.CaptureTime 123123123123 \
    --Alerts.0.MoveAlert.Move True \
    --Alerts.0.MoveAlert.MoveConfidence 0.32 \
    --Alerts.0.CoverAlert.Cover True \
    --Alerts.0.CoverAlert.CoverConfidence 0.32
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

