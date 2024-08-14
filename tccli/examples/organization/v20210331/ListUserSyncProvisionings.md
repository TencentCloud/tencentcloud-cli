**Example 1: 查询CAM用户同步列表**

查询CAM用户同步列表

Input: 

```
tccli organization ListUserSyncProvisionings --cli-unfold-argument  \
    --ZoneId z-dsjsisnus \
    --PrincipalId u-sjs9smss \
    --NextToken  \
    --MaxResults 10 \
    --PrincipalType User \
    --TargetUin 100003324902 \
    --TargetType MemberUin \
    --Filter test
```

Output: 
```
{
    "Response": {
        "NextToken": "OTM0YzE4MzY2ZjdhMWM0MYZDhnYaxsiYTLI=",
        "TotalCounts": 30,
        "MaxResults": 10,
        "IsTruncated": true,
        "UserProvisionings": [
            {
                "UserProvisioningId": "up-siwnei3nso",
                "Description": "this is cam user sync",
                "Status": "Enabled",
                "PrincipalId": "u-swnd8wn3",
                "PrincipalName": "test",
                "PrincipalType": "User",
                "TargetUin": "10000338332",
                "TargetName": "test",
                "DuplicationStrategy": "KeepBoth",
                "DeletionStrategy": "Delete",
                "CreateTime": "2024-01-01 12:12:12",
                "UpdateTime": "2024-01-01 12:12:12",
                "TargetType": "MemberUin"
            }
        ],
        "RequestId": "e297543a-80de-4039-83c8-9d35d4545"
    }
}
```

