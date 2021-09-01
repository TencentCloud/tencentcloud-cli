**Example 1: 获取资源授权列表**



Input: 

```
tccli cme DescribeResourceAuthorization --cli-unfold-argument  \
    --Platform test \
    --Operator 123 \
    --Owner.Type TEAM \
    --Owner.Id teamA \
    --Resources.0.Type MATERIAL \
    --Resources.0.Id mid_abc
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

