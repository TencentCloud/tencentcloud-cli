**Example 1: 合同催办**

针对合同流程中尚未完成签署的用户发送催办消息。
部分合同流程可以催办，而部分则无法催办。
通过查看返回的详细信息清单，可了解各合同流程的催办结果。

Input: 

```
tccli ess CreateFlowReminds --cli-unfold-argument  \
    --Operator.UserId yDxMkUyxxxxxxxxxxxVI2JmKxPkk \
    --FlowIds yDwXiUUc******************SZ0uIW72Qaxm yDwFmUU******************BSat8PWOt2iQF
```

Output: 
```
{
    "Response": {
        "RemindFlowRecords": [
            {
                "CanRemind": true,
                "FlowId": "yDwXiUUc******************SZ0uIW72Qaxm",
                "RemindMessage": ""
            },
            {
                "CanRemind": false,
                "FlowId": "yDwFmUU******************BSat8PWOt2iQF",
                "RemindMessage": "签署人 xxx: 此签署人已催办过"
            }
        ],
        "RequestId": "s16*********203499"
    }
}
```

