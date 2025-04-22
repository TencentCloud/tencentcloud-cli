**Example 1: 搜索运维任务执行结果**

搜索运维任务执行结果

Input: 

```
tccli bh SearchTaskResult --cli-unfold-argument  \
    --UserName nick \
    --Name nic \
    --Limit 1 \
    --StartTime 2020-09-22T00:00:00+08:00 \
    --Offset 1 \
    --EndTime 2020-09-22T00:00:00+08:00 \
    --OperationId ops-aeqwcaw \
    --TaskType 1 2 \
    --RealName tom
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "c241022e-c50d-47b2-9748-691a09c143c4",
        "TaskResult": [
            {
                "UserName": "nick",
                "Status": 0,
                "Name": "nic",
                "FromIp": "192.168.0.1",
                "StartTime": "2020-09-22T00:00:00+08:00",
                "EndTime": "2020-09-22T00:00:00+08:00",
                "Id": "1",
                "RealName": "tom",
                "OperationId": "ops-adexdea"
            }
        ]
    }
}
```

