**Example 1: 查询虚拟连接**



Input: 

```
tccli vpc DescribeCdcNetPlanes --cli-unfold-argument  \
    --Filters.0.Name cdc-id \
    --Filters.0.Values cluster-d8htgb6k \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "CdcNetPlaneSet": [
            {
                "NetPlaneId": "np-823f905a",
                "VpcIds": [],
                "CdcId": "cluster-d8htgb6k",
                "Name": "1122",
                "Description": "",
                "CreateTime": "2024-01-10T17:10:14.762252",
                "UpdateTime": "2024-01-10T17:30:49.678059"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ae3f0435-4724-42df-a6c6-239391af0926"
    }
}
```

