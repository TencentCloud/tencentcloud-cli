**Example 1: DescribeSpaceFenceEventList**

获取位置空间下围栏告警事件列表

Input: 

```
tccli iotexplorer DescribeSpaceFenceEventList --cli-unfold-argument  \
    --SpaceId 5bf5407370cc40848f39a2896a2ab052 \
    --StartTime 1604030050000 \
    --EndTime 1604039050000 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ProductId": "X4912BAIVR",
                "DeviceName": "dev1",
                "FenceId": 6,
                "AlertType": "In",
                "Data": {
                    "AlarmTime": 1604034069575,
                    "Longitude": 113.95,
                    "Latitude": 22.55782
                }
            }
        ],
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e",
        "Total": 1
    }
}
```

