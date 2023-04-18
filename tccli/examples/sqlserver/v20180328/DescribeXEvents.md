**Example 1: DescribeXEvents**

查询实例的扩展事件记录，包括慢SQL、阻塞、死锁

Input: 

```
tccli sqlserver DescribeXEvents --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --StartTime 2023-03-05 11:49:08 \
    --EndTime 2023-03-13 11:49:08 \
    --EventType slow \
    --InstanceId mssql-qp7gu6ch
```

Output: 
```
{
    "Response": {
        "RequestId": "023a2da2-c152-11ed-b1aa-525400853186",
        "TotalCount": 10,
        "Events": [
            {
                "EndTime": "2023-03-10 15:45:05",
                "EventType": "slow",
                "ExternalAddr": "https://***",
                "FileName": "autoed_instance_58001_20230220110419.xel",
                "Id": 1004,
                "InternalAddr": "https:***",
                "Size": 10240,
                "StartTime": "2023-03-10 15:44:15",
                "Status": 1
            }
        ]
    }
}
```

