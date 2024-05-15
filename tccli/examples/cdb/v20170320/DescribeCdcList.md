**Example 1: 查询本地专属集群列表**



Input: 

```
tccli cdb DescribeCdcList --cli-unfold-argument  \
    --CdcIds cluster_cdc_test \
    --CdcName abc \
    --NeedDetails True \
    --IncludeOff True \
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
                "CdcId": "cluster_cdc_test",
                "ZoneId": 10006,
                "Zone": "abc",
                "CdcName": "abc",
                "Status": "abc",
                "ClusterType": 1,
                "CampusId": 1,
                "DeviceClass": "abc",
                "ExclusterId": "abc"
            }
        ],
        "RequestId": "39db5967-5605-42e0-b7b6-36cb74e5f8a7"
    }
}
```

