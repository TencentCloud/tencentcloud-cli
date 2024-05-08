**Example 1: 查询设备云存 AI 分析任务列表**



Input: 

```
tccli iotexplorer DescribeCloudStorageAIServiceTasks --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D \
    --DeviceName aaa_31400554_1 \
    --ServiceType PackageDetect \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "TaskId": "fb066d7a-baac-4706-acda-058f56f82759",
                "ProductId": "TQBDY6RPI9",
                "DeviceName": "cs_112114601_2",
                "ChannelId": 0,
                "ServiceType": "PackageDetect",
                "StartTime": 1710487888,
                "EndTime": 1710487898,
                "Status": 3,
                "Result": "{\"param1\":\"value1\"}",
                "Files": [
                    "output.mp4"
                ],
                "CreateTime": 1710490000,
                "UpdateTime": 1710490000
            }
        ],
        "Total": 1,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

