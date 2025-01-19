**Example 1: 查询视频浓缩结果列表**



Input: 

```
tccli iotexplorer DescribeCloudStorageAIServiceTasks --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D \
    --DeviceName aaa_31400554_1 \
    --ServiceType Highlight \
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
                "Result": "",
                "Files": [
                    "highlight.mp4",
                    "thumbnail.jpg"
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

**Example 2: 查询视频语义理解结果列表**



Input: 

```
tccli iotexplorer DescribeCloudStorageAIServiceTasks --cli-unfold-argument  \
    --ProductId TSLFHRWDSD \
    --DeviceName dev004 \
    --ServiceType VideoToText \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "b97d82c1-bf0b-421b-a2c1-cc5053c214ea",
        "Tasks": [
            {
                "ChannelId": 0,
                "CreateTime": 1736994466,
                "DeviceName": "dev004",
                "EndTime": 1736994458,
                "Files": [],
                "ProductId": "TSLFHRWDSD",
                "Result": "{\"DetectedClassifications\": [\"person\"], \"Summary\": \"一个人在雨天街道上行走\"}",
                "ServiceType": "VideoToText",
                "StartTime": 1736994450,
                "Status": 3,
                "TaskId": "01946cf0-27ee-7ebc-b3a3-5ae31ff61424",
                "UpdateTime": 1736994478
            }
        ],
        "Total": 1
    }
}
```

