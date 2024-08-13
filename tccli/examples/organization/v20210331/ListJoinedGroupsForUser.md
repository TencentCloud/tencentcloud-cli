**Example 1: 查询用户加入的用户组**

查询用户加入的用户组

Input: 

```
tccli organization ListJoinedGroupsForUser --cli-unfold-argument  \
    --ZoneId z-2o3meo3 \
    --UserId u-3od3e3d \
    --NextToken  \
    --MaxResults 10
```

Output: 
```
{
    "Response": {
        "NextToken": "OTM0YzE4MzY2ZjdhMWM0MYZDhnYaxsiYTLI=",
        "TotalCounts": 20,
        "MaxResults": 10,
        "IsTruncated": true,
        "JoinedGroups": [
            {
                "GroupName": "testGroup",
                "Description": "this is testGroup",
                "GroupId": "g-s23nw3e",
                "GroupType": "Manual",
                "JoinTime": "2021-01-01 12:12:12"
            }
        ],
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

