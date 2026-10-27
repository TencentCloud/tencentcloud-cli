**Example 1: 查询任务执行的详细情况**



Input: 

```
tccli cvd DescribeInvocationDetail --cli-unfold-argument  \
    --InstanceId cdi-234r32ad \
    --OutputLinesOffset 1 \
    --OutputLinesLimit 1 \
    --InvokeId 23sfc-324-s11
```

Output: 
```
{
    "Response": {
        "Detail": {
            "Status": "Finished",
            "Output": {
                "Encoding": "PlainText",
                "Lines": [
                    "23radef"
                ],
                "AllLinesOffset": 1,
                "LinesOffset": 1,
                "AllLinesNum": 1,
                "LinesNum": 1
            },
            "InvokeId": "23sfc-324-s11",
            "ErrorCode": "",
            "ErrorInfo": ""
        },
        "RequestId": "a4c33d6d-d6a2-47d3-9a19-940ead9f8752"
    }
}
```

