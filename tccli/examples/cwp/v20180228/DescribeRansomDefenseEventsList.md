**Example 1: 查询防勒索事件列表**

根据过滤参数查询防勒索事件列表

Input: 

```
tccli cwp DescribeRansomDefenseEventsList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": "xx",
                "BaitFilePath": "xx",
                "Uuid": "xx",
                "FilePath": "xx",
                "InstanceId": "xx",
                "HostName": "xx",
                "Pid": 1,
                "FileMd5": "xx",
                "CreateTime": "xx",
                "Quuid": "xx",
                "PidParam": "xx",
                "ModifyTime": "xx",
                "WanIp": "xx",
                "StrategyId": 1,
                "HostIp": "xx",
                "Type": 1,
                "Id": 1,
                "StrategyName": "xx",
                "FileSize": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

