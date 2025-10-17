**Example 1: 查询表的分区详情信息**

查询表的分区详情信息

Input: 

```
tccli wedata DescribeTablePartitions --cli-unfold-argument  \
    --PageNumber 0 \
    --TableId guid \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "",
        "TablePartitionSet": [
            {
                "ModifiedTime": "2020-09-22T00:00:00+00:00",
                "RecordCount": 0,
                "StorageSizeWithUnit": "",
                "PartitionName": "",
                "StorageSize": "10",
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ]
    }
}
```

