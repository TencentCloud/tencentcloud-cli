**Example 1: 请求demo**



Input: 

```
tccli wedata DescribeExecutionLog --cli-unfold-argument  \
    --InstanceId 202401011212131209_09:23:23 \
    --RecordId 123 \
    --DetailId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "5add3416-a58b-4cfe-b488-c678c700007e",
        "InstanceId": "202401011212131209_09:23:23",
        "Logs": [
            "test"
        ],
        "DetailId": 123,
        "DetailStatus": "SUCCESS"
    }
}
```

