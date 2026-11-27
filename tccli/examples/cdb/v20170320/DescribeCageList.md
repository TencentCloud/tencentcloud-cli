**Example 1: 查询金融围拢、独享集群列表**



Input: 

```
tccli cdb DescribeCageList --cli-unfold-argument  \
    --CageIds cluster_cdc \
    --CageName 广州独享集群 \
    --ZoneId 10006 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "CageId": "cluster_cdc",
                "ZoneId": 10006,
                "CageName": "广州独享集群",
                "Status": "OFF",
                "ZoneIds": [
                    10003,
                    10004
                ]
            }
        ],
        "RequestId": "39db5967-5605-42e0-b7b6-36cb74e5f8a7"
    }
}
```

