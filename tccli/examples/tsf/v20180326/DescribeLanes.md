**Example 1: 查询泳道配置列表**



Input: 

```
tccli tsf DescribeLanes --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --SearchWord lane \
    --LaneIdList lane-ynmlnwm4 \
    --DisableProgramAuthCheck True
```

Output: 
```
{
    "Response": {
        "RequestId": "c6dec7e1-dfcd-4a12-8977-986605343663",
        "Result": {
            "Content": [
                {
                    "CreateTime": 1726849955000,
                    "Entrance": null,
                    "LaneGroupList": null,
                    "LaneId": "lane-ynmlnwm4",
                    "LaneName": "lane_name",
                    "NamespaceIdList": null,
                    "Remark": "",
                    "UpdateTime": 1726849955000
                }
            ],
            "TotalCount": 1
        }
    }
}
```

