**Example 1: 请求demo**



Input: 

```
tccli wedata DescribeTestRun --cli-unfold-argument  \
    --InstanceKey 20230101121232123_20:12:23 \
    --CurrRunDate 20:12:23 \
    --TaskId 20230101121232123
```

Output: 
```
{
    "Response": {
        "Status": "SUCCESS",
        "Finished": true,
        "LogContent": "test",
        "InstanceKey": "20230101121232123_20:12:23",
        "RequestId": "ef431542-96ae-467c-b821-f594df8ac83c"
    }
}
```

