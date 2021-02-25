**Example 1: 多经点位配置更新**



Input: 

```
tccli ump ModifyMultiBizConfig --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --CameraId 1 \
    --ZoneId 1 \
    --MonitoringAreas.0.Points.0.X 1 \
    --MonitoringAreas.0.Points.0.Y 1 \
    --MonitoringAreas.0.Points.1.X 2 \
    --MonitoringAreas.0.Points.1.Y 2 \
    --MonitoringAreas.0.Points.2.X 3 \
    --MonitoringAreas.0.Points.2.Y 3 \
    --MonitoringAreas.0.Points.3.X 4 \
    --MonitoringAreas.0.Points.3.Y 4
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

