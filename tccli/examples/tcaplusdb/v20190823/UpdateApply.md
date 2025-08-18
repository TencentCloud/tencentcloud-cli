**Example 1: 更新申请单状态**

更新申请单状态

Input: 

```
tccli tcaplusdb UpdateApply --cli-unfold-argument  \
    --ApplyStatus.0.ApplicationId 121421 \
    --ApplyStatus.0.ApplicationStatus 0 \
    --ApplyStatus.0.ApplicationType 0 \
    --ApplyStatus.0.ClusterId 1984343
```

Output: 
```
{
    "Response": {
        "ApplyResults": [
            {
                "ApplicationId": "121421",
                "ApplicationStatus": 0,
                "ApplicationType": 7,
                "Error": {
                    "Code": "OperationDenied",
                    "Message": "Application has been processed."
                },
                "TaskId": "32425"
            }
        ],
        "RequestId": "2324324-3534",
        "TotalCount": 0
    }
}
```

