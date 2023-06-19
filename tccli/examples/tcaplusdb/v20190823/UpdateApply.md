**Example 1: 更新申请单状态**

更新申请单状态

Input: 

```
tccli tcaplusdb UpdateApply --cli-unfold-argument  \
    --ApplyStatus.0.ApplicationId abc \
    --ApplyStatus.0.ApplicationStatus 0 \
    --ApplyStatus.0.ApplicationType 0 \
    --ApplyStatus.0.ClusterId abc
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

