**Example 1: 获取投递任务列表**



Input: 

```
tccli cls DescribeShipperTasks --cli-unfold-argument  \
    --ShipperId 53d355bc-9814-43b4-b10a-4be50405095f \
    --StartTime 1753766424000 \
    --EndTime 1753780282000
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "TaskId": "000000f3-1b0a-444b-bb64-2e64455239e4",
                "ShipperId": "53d355bc-9814-43b4-b10a-4be50405095f",
                "TopicId": "5b158596-d0ad-4da5-af92-4fac4cd662c4",
                "RangeStart": "1753764300000",
                "RangeEnd": "1753764600000",
                "StartTime": "1753766424000",
                "EndTime": "1753780282000",
                "Status": "success",
                "Message": "success"
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

