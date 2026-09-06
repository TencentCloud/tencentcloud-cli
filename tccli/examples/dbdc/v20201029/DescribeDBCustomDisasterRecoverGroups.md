**Example 1: 查询置放群组列表**



Input: 

```
tccli dbdc DescribeDBCustomDisasterRecoverGroups --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "DisasterRecoverGroupSet": [
            {
                "Affinity": 1,
                "CreatedTime": "2026-08-27T23:14:01Z",
                "CurrentNum": 0,
                "DisasterRecoverGroupId": "dbps-9u4mlmcx",
                "Name": "置放群组",
                "NodeIds": [],
                "NodeQuotaTotal": 50,
                "Status": "Available",
                "Strategy": "SPREAD",
                "Tags": null,
                "Type": "HOST"
            }
        ],
        "TotalCount": 2,
        "RequestId": "ea6358e7-2baa-42d4-bd66-f25a7d4fe8e0"
    }
}
```

