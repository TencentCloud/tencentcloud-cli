**Example 1: 查询云桌面上的任务列表**



Input: 

```
tccli cvd DescribeInvocations --cli-unfold-argument  \
    --InstanceId cdi-232fsacsef11
```

Output: 
```
{
    "Response": {
        "RequestId": "ccadfb61-c65f-4e17-b7d0-a477fce19f10",
        "Invocations": [
            {
                "Status": "Finished",
                "Output": null,
                "InvokeId": "23sfc-324-s11",
                "ErrorCode": "",
                "ErrorInfo": ""
            }
        ]
    }
}
```

