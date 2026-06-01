**Example 1: DescribeSqlHistoryRecords**

sql在线运行记录

Input: 

```
tccli tchousex DescribeSqlHistoryRecords --cli-unfold-argument  \
    --InstanceId abc \
    --QueryOnlineLogReq.StartTime 0 \
    --QueryOnlineLogReq.EndTime 0 \
    --QueryOnlineLogReq.Offset 0 \
    --QueryOnlineLogReq.Limit 0 \
    --QueryOnlineLogReq.QueryID abc \
    --QueryOnlineLogReq.SubmitUser abc \
    --QueryOnlineLogReq.State abc \
    --QueryOnlineLogReq.StartTimeOrder abc \
    --QueryOnlineLogReq.ExecuteTimeOrder abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "QueryOnlineLogRes": [
            {
                "QueryID": "abc",
                "Statement": "abc",
                "State": "abc",
                "SubmitUser": "abc",
                "StartTime": "abc",
                "Duration": 0
            }
        ],
        "Count": 0,
        "RequestId": "abc"
    }
}
```

