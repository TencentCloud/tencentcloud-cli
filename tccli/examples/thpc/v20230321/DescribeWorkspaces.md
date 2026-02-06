**Example 1: 查询工作空间列表**

查看在上海8区的实例信息,限制返回结果最多为一项

Input: 

```
tccli thpc DescribeWorkspaces --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values ap-shanghai-8 \
    --Filters.0.Name zone \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0142a337-d8cf-4ae1-857f-d090c1f802fdafd",
        "SpaceSet": [
            {
                "CreatedTime": "2024-09-22T00:00:00+00:00",
                "ExpiredTime": "2024-09-22T00:00:00+00:00",
                "LatestOperation": "CreateWorkspaces",
                "LatestOperationState": "SUCCESS",
                "Placement": {
                    "Zone": "ap-shanghai-8"
                },
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "ResourceId": "ins-3zjugd6z",
                "SpaceChargeType": "PREPAID",
                "SpaceFamily": "96AS",
                "SpaceId": "wks-bfdafadfd",
                "SpaceName": "workspace",
                "SpaceState": "ONLINE",
                "SpaceType": "96AS.4XLARGE160",
                "Tags": []
            }
        ],
        "TotalCount": 1
    }
}
```

