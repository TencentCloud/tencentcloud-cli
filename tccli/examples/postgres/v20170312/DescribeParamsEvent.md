**Example 1: 获取实例参数修改事件列表**

获取参数修改状态、记录

Input: 

```
tccli postgres DescribeParamsEvent --cli-unfold-argument  \
    --DBInstanceId postgres-nbvqjlhf
```

Output: 
```
{
    "Response": {
        "EventItems": [
            {
                "EventCount": 1,
                "EventDetail": [
                    {
                        "EffectiveTime": "0001-01-01 00:00:00",
                        "EventLog": "",
                        "ModifyTime": "2021-08-11 21:51:12",
                        "NewValue": "off",
                        "OldValue": "on",
                        "Operator": "100130115276",
                        "ParamName": "array_nulls",
                        "State": "success"
                    }
                ],
                "ParamName": "array_nulls"
            },
            {
                "EventCount": 1,
                "EventDetail": [
                    {
                        "EffectiveTime": "2021-08-16 15:33:41",
                        "EventLog": "Pause: Paused. Internal error, in manual processing",
                        "ModifyTime": "2021-08-16 15:28:13",
                        "NewValue": "7",
                        "OldValue": "8",
                        "Operator": "100000115276",
                        "ParamName": "max_worker_processes",
                        "State": "paused"
                    }
                ],
                "ParamName": "max_worker_processes"
            }
        ],
        "RequestId": "",
        "TotalCount": 2
    }
}
```

