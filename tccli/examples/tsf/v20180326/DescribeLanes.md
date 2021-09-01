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
    "RequestId": "fd8664ea-458d-41b6-b22e-a1e1194e6246",
    "Result": {
        "TotalCount": 2,
        "Content": [
            {
                "LaneId": "lane-6ymrl35a",
                "LaneName": "11",
                "Remark": "11",
                "CreateTime": 1586848711000,
                "UpdateTime": 1586848711000,
                "LaneGroupList": null,
                "Entrance": null,
                "NamespaceIdList": null
            },
            {
                "LaneId": "lane-6ymrl42a",
                "LaneName": "111",
                "Remark": "111",
                "CreateTime": 1586340248000,
                "UpdateTime": 1586340248000,
                "LaneGroupList": null,
                "Entrance": null,
                "NamespaceIdList": null
            }
        ]
    }
}
```

