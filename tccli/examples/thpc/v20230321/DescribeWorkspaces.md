**Example 1: 查询工作空间列表**

查看在广州二区的实例信息,限制返回结果最多为一项

Input: 

```
tccli thpc DescribeWorkspaces --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values ap-guangzhou-2 \
    --Filters.0.Name zone \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SpaceSet": [
            {
                "SpaceId": "abc",
                "SpaceFamily": "abc",
                "SpaceType": "abc",
                "SpaceName": "abc",
                "SpaceState": "abc",
                "SpaceChargeType": "abc",
                "ResourceId": "abc",
                "RenewFlag": "abc",
                "Tags": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "ExpiredTime": "2020-09-22T00:00:00+00:00",
                "Placement": {
                    "Zone": "abc"
                },
                "LatestOperation": "abc",
                "LatestOperationState": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

