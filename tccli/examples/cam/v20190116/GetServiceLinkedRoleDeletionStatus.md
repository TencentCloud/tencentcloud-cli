**Example 1: Getting the status of the service-linked role deletion**



Input: 

```
tccli cam GetServiceLinkedRoleDeletionStatus --cli-unfold-argument  \
    --DeletionTaskId 100
```

Output: 
```
{
    "Response": {
        "Status": "SUCCEEDED",
        "ServiceType": "cam",
        "ServiceName": "CAM",
        "Reason": "{}",
        "RequestId": "c3da1c1c-df35-467d-9335-99c68d993e0a"
    }
}
```

