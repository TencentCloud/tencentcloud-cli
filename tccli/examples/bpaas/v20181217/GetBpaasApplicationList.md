**Example 1: 获取申请列表**



Input: 

```
tccli bpaas GetBpaasApplicationList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "ApplicationList": [
            {
                "ApplicationId": 1000000001,
                "BpaasId": 1000000001,
                "BpaasName": "ww",
                "Status": 1,
                "CreateTime": "2020-06-09 18:54:36",
                "Users": [],
                "NodeId": "",
                "ApproveMethod": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "1e7d1633-0fff-474d-a980-5c79d1233440"
    }
}
```

