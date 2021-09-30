**Example 1: 指定独享集群ID查询集群详情。**

部分用户(金融)对cbs集群有独享需求，该接口用来查询用户所拥有的独享集群。

Input: 

```
tccli cbs DescribeDiskStoragePool --cli-unfold-argument  \
    --Filters.0.Name cdc-id \
    --Filters.0.Values cdc-6brr1cvj
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "DiskStoragePoolSet": [
            {
                "CageId": "xx",
                "CdcState": "xx",
                "Zone": "xx",
                "CdcName": "xx",
                "CdcResource": {
                    "DiskAavilable": 1,
                    "DiskTotal": 1
                },
                "CdcId": "xx",
                "DiskType": "xx",
                "ExpiredTime": "2020-09-22 00:00:00"
            }
        ]
    }
}
```

