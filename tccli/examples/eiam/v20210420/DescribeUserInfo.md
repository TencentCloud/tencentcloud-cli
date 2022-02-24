**Example 1: 请求示例**



Input: 

```
tccli eiam DescribeUserInfo --cli-unfold-argument  \
    --UserName xxx
```

Output: 
```
{
    "Response": {
        "UserName": "xx",
        "Status": "xx",
        "DisplayName": "xx",
        "Description": "xx",
        "SecondaryOrgNodeIdList": [
            "xx"
        ],
        "UserGroupIds": [
            "xx",
            "xx"
        ],
        "AdminFlag": 1,
        "UserId": "xx",
        "Phone": "xx",
        "OrgNodeId": "xx",
        "DataSource": "xx",
        "Email": "xx",
        "ExpirationTime": "xx",
        "ActivationTime": "xx",
        "PwdNeedReset": true,
        "RequestId": "xx"
    }
}
```

