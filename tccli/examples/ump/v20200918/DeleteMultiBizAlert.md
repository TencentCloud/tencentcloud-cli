**Example 1: 多经点位消警**



Input: 

```
tccli ump DeleteMultiBizAlert --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --CameraId 1 \
    --ZoneId 1 \
    --ActionType 1 \
    --Image imagebase64string
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

