**Example 1: 获取媒资授权信息**



Input: 

```
tccli cme DescribeResourceAuthorization --cli-unfold-argument  \
    --Platform test \
    --Operator 123 \
    --Owner.Type TEAM \
    --Owner.Id teamA \
    --Resource.Type MATERIAL \
    --Resource.Id mid_abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AuthorizationInfoSet": [
            {
                "Authorizee": {
                    "Type": "PERSON",
                    "Id": "234"
                },
                "PermissionSet": [
                    "R",
                    "W"
                ]
            }
        ],
        "RequestId": "requestId"
    }
}
```

