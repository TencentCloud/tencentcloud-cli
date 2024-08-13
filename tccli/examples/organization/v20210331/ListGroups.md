**Example 1: 查询用户组列表**

查询用户组列表

Input: 

```
tccli organization ListGroups --cli-unfold-argument  \
    --ZoneId z-32s7dhd8s*** \
    --MaxResults 20 \
    --GroupType Manual
```

Output: 
```
{
    "Response": {
        "NextToken": "OTM0YzE4MzY2ZjdhMWM0MYZD******",
        "Groups": [
            {
                "GroupName": "testGroup",
                "Description": "thsi is group",
                "CreateTime": "2024-01-01 12:12:12",
                "GroupType": "Manual",
                "UpdateTime": "2024-01-01 12:12:12",
                "GroupId": "g-q8shs8h****",
                "MemberCount": 20
            }
        ],
        "MaxResults": 10,
        "TotalCounts": 30,
        "IsTruncated": true,
        "RequestId": "e297543a-80de-4039-83c8-9d35d4545"
    }
}
```

