**Example 1: 更新申请单状态**



Input: 

```
tccli tcaplusdb UpdateApply --cli-unfold-argument  \
    --ApplyStatus.0.ApplicationStatus 1 \
    --ApplyStatus.0.ClusterId xx \
    --ApplyStatus.0.ApplicationId xx \
    --ApplyStatus.0.ApplicationType 7
```

Output: 
```
{
    "Response": {
        "ApplyResults": [
            {
                "ApplicationId": "2-273",
                "ApplicationStatus": null,
                "ApplicationType": 7,
                "Error": {
                    "Code": "OperationDenied",
                    "Message": "Application has been processed."
                },
                "TaskId": null
            }
        ],
        "RequestId": "fdsfdsfdsfdsf",
        "TotalCount": 0
    }
}
```

