**Example 1: 查询安全日志告警信息**



Input: 

```
tccli tcss DescribeSecLogAlertMsg --cli-unfold-argument  \
    --Type log_reserve_full
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "MsgValue": "xx",
                "MsgType": "xx",
                "State": true
            }
        ],
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

