**Example 1: 获取媒资授权信息**



Input: 

```
tccli cme DescribeResourceAuthorization --cli-unfold-argument  \
    --Operator cmeid_system \
    --Platform 1000000001 \
    --Resource.Type MATERIAL \
    --Resource.Id 67e105de4fb8950001052fff \
    --Owner.Type TEAM \
    --Owner.Id b718fcee09a72470bf665cffff
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
                    "Id": "d1c5eb0ee4994419b46560"
                },
                "PermissionSet": [
                    "R",
                    "W"
                ]
            }
        ],
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb65b"
    }
}
```

