**Example 1: 获取投递任务列表**



Input: 

```
tccli cls DescribeShipperTasks --cli-unfold-argument  \
    --ShipperId xxxxx-xxx-xx-xxx-xxxxx \
    --StartTime 978653222 \
    --EndTime 978653333
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "TaskId": "xxxxx-xx-xx-xx",
                "ShipperId": "xxxxx-xx-xx-xx",
                "TopicId": "xxxxx-xx-xx-xx",
                "RangeStart": "978653222",
                "RangeEnd": "978653222",
                "StartTime": "978653222",
                "EndTime": "978653222",
                "Status": "success",
                "Message": "success"
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

