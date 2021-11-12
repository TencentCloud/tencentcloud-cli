**Example 1: 查询泳道列表**



Input: 

```
tccli tsf DescribeLanes --cli-unfold-argument  \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "Remark": "xx",
                    "Entrance": true,
                    "UpdateTime": 0,
                    "LaneId": "xx",
                    "NamespaceIdList": [
                        "xx"
                    ],
                    "LaneGroupList": [
                        {
                            "ApplicationName": "xx",
                            "Entrance": true,
                            "NamespaceName": "xx",
                            "LaneGroupId": "xx",
                            "UpdateTime": 0,
                            "ClusterType": "xx",
                            "GroupName": "xx",
                            "LaneId": "xx",
                            "NamespaceId": "xx",
                            "GroupId": "xx",
                            "ApplicationId": "xx",
                            "CreateTime": 0
                        }
                    ],
                    "LaneName": "xx",
                    "CreateTime": 0
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "xx"
    }
}
```

