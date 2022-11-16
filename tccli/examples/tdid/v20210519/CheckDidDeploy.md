**Example 1: CheckDidDeploy**

检查部署情况

Input: 

```
tccli tdid CheckDidDeploy --cli-unfold-argument  \
    --TaskId 37
```

Output: 
```
{
    "Response": {
        "Task": {
            "Id": 37,
            "AppId": 251005746,
            "ClusterId": "bcos-fmtkyt8xne",
            "GroupId": 6,
            "ServiceId": 0,
            "Status": 0,
            "ErrorCode": "",
            "ErrorMsg": "",
            "CreateTime": "2021-07-23 13:52:50",
            "UpdateTime": "2021-07-23 13:52:50"
        },
        "RequestId": ""
    }
}
```

