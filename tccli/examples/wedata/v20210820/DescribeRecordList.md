**Example 1: 获取任务列表**

获取任务列表

Input: 

```
tccli wedata DescribeRecordList --cli-unfold-argument  \
    --ScriptId abc \
    --SqlStatement abc \
    --StartTime 1 \
    --EndTime 1 \
    --Status abc \
    --PageIndex 1 \
    --PageSize 1 \
    --ScriptType abc \
    --IsOnlyMyselfDebug True
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Id": 1,
                "ScriptContent": "abc",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "Status": "abc",
                "Details": [
                    {
                        "Id": 1,
                        "StartTime": "2020-09-22T00:00:00+00:00",
                        "EndTime": "2020-09-22T00:00:00+00:00",
                        "Status": "abc",
                        "ScriptContent": "abc",
                        "RecordId": 1,
                        "Duration": "abc"
                    }
                ],
                "InstanceId": "abc",
                "ExecutorId": "abc",
                "ExecutorDisplayName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

