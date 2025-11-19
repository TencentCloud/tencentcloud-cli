**Example 1: 示例一**

示例一

Input: 

```
tccli dlc DescribeTablePartitions --cli-unfold-argument  \
    --Catalog DataLakeCatalog \
    --Database wd_262 \
    --Table pt_string \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "MixedPartitions": {
            "IcebergPartitions": [
                {
                    "CreateTime": "2024-06-14T14:40:21.417+08:00",
                    "DataFileSize": 1,
                    "DataFileStorage": 627,
                    "LastUpdateSnapshotId": "1440430386687553985",
                    "Partition": "pt=xyz",
                    "Records": 1,
                    "UpdateTime": "2024-06-14T14:40:21.417+08:00"
                },
                {
                    "CreateTime": "2024-06-14T14:38:14.37+08:00",
                    "DataFileSize": 1,
                    "DataFileStorage": 627,
                    "LastUpdateSnapshotId": "2427096367833466031",
                    "Partition": "pt=abc",
                    "Records": 1,
                    "UpdateTime": "2024-06-14T14:38:14.37+08:00"
                },
                {
                    "CreateTime": "2024-06-14T14:40:17.59+08:00",
                    "DataFileSize": 1,
                    "DataFileStorage": 627,
                    "LastUpdateSnapshotId": "4824566865672576224",
                    "Partition": "pt=efg",
                    "Records": 1,
                    "UpdateTime": "2024-06-14T14:40:17.59+08:00"
                }
            ],
            "TableFormat": "ICEBERG",
            "TotalSize": 3
        },
        "RequestId": "8d15ab5d-164f-462a-b82c-ead5891c3b6c"
    }
}
```

**Example 2: 示例二**



Input: 

```
tccli dlc DescribeTablePartitions --cli-unfold-argument  \
    --Catalog DataLakeCatalog \
    --Database perf_orc_100 \
    --Table store_returns \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "MixedPartitions": {
            "HivePartitions": [
                {
                    "CreateTime": "2022-07-26T16:10:52+08:00",
                    "DataFileStorage": 0,
                    "LastAccessTime": "2022-07-26T16:10:52+08:00",
                    "ModifiedTime": "2022-07-26T16:10:52+08:00",
                    "Partition": "sr_returned_date_sk=2452817",
                    "Records": 0
                },
                {
                    "CreateTime": "2022-07-26T16:10:52+08:00",
                    "DataFileStorage": 0,
                    "LastAccessTime": "2022-07-26T16:10:52+08:00",
                    "ModifiedTime": "2022-07-26T16:10:52+08:00",
                    "Partition": "sr_returned_date_sk=2452816",
                    "Records": 0
                },
                {
                    "CreateTime": "2022-07-26T16:10:52+08:00",
                    "DataFileStorage": 0,
                    "LastAccessTime": "2022-07-26T16:10:52+08:00",
                    "ModifiedTime": "2022-07-26T16:10:52+08:00",
                    "Partition": "sr_returned_date_sk=2452815",
                    "Records": 0
                },
                {
                    "CreateTime": "2022-07-26T16:10:52+08:00",
                    "DataFileStorage": 0,
                    "LastAccessTime": "2022-07-26T16:10:52+08:00",
                    "ModifiedTime": "2022-07-26T16:10:52+08:00",
                    "Partition": "sr_returned_date_sk=2452814",
                    "Records": 0
                }
            ],
            "TableFormat": "HIVE",
            "TotalSize": 2004
        },
        "RequestId": "4b9f8cdb-4fc0-4de0-8573-171531e55d74"
    }
}
```

