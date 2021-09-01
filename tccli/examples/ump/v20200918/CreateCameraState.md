**Example 1: 相机状态上报接口**



Input: 

```
tccli ump CreateCameraState --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --CameraStates.0.CameraId 1 \
    --CameraStates.0.State 10 \
    --CameraStates.1.CameraId 2 \
    --CameraStates.1.State 11
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

