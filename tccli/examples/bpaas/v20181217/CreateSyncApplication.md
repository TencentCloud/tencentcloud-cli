**Example 1: 发起异步审批流申请**

发起异步审批流申请

Input: 

```
tccli bpaas CreateSyncApplication --cli-unfold-argument  \
    --UniqueId 1111 \
    --ApplicationParams.0.Key name \
    --ApplicationParams.0.Value test \
    --ApplicationParams.0.Name test \
    --Reason test
```

Output: 
```
{
    "Response": {
        "ApplicationId": 1,
        "RequestId": "3c140219-cfe9-470e-b241-90787*****03"
    }
}
```

