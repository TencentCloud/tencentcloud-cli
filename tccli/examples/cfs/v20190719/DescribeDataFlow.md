**Example 1: 查询数据流动**



Input: 

```
tccli cfs DescribeDataFlow --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DataFlows": [
            {
                "CreationTime": "2025-06-10 10:23:28",
                "DataFlowId": "cfs-dataflow-23e12b77",
                "DataFlowName": "aileen-test",
                "FileSystemId": "cfs-4551ef87e",
                "SourcePath": "test3",
                "SourceStorageAddress": "https://aileen-data-flow-1251000004.cos.ap-guangzhou.myqcloud.com",
                "SourceStorageType": "S3_COS",
                "Status": "available",
                "TargetPath": "/cfs/test3/"
            },
            {
                "CreationTime": "2025-06-10 15:01:26",
                "DataFlowId": "cfs-dataflow-dcee19a7",
                "DataFlowName": "aileen-test",
                "FileSystemId": "cfs-4551ef87e",
                "SourcePath": "test4",
                "SourceStorageAddress": "https://aileen-data-flow-1251000001.cos.ap-guangzhou.myqcloud.com",
                "SourceStorageType": "S3_COS",
                "Status": "available",
                "TargetPath": "/cfs/test4/"
            },
            {
                "CreationTime": "2025-06-10 15:01:45",
                "DataFlowId": "cfs-dataflow-13ff99f9",
                "DataFlowName": "aileen-test",
                "FileSystemId": "cfs-44d53b63e",
                "SourcePath": "test4",
                "SourceStorageAddress": "https://aileen-data-flow-1251000001.cos.ap-guangzhou.myqcloud.com",
                "SourceStorageType": "S3_COS",
                "Status": "available",
                "TargetPath": "/cfs/test8/"
            },
            {
                "CreationTime": "2025-06-10 15:01:53",
                "DataFlowId": "cfs-dataflow-7368df7c",
                "DataFlowName": "aileen-test",
                "FileSystemId": "cfs-44d53b63e",
                "SourcePath": "test3",
                "SourceStorageAddress": "https://aileen-data-flow-1251000001.cos.ap-guangzhou.myqcloud.com",
                "SourceStorageType": "S3_COS",
                "Status": "available",
                "TargetPath": "/cfs/test9/"
            },
            {
                "CreationTime": "2025-06-10 15:23:25",
                "DataFlowId": "cfs-dataflow-4f827203",
                "DataFlowName": "test",
                "FileSystemId": "cfs-44d53b63e",
                "SourcePath": "test3",
                "SourceStorageAddress": "https://aileen-data-flow-1251000001.cos.ap-guangzhou.myqcloud.com",
                "SourceStorageType": "S3_COS",
                "Status": "available",
                "TargetPath": "/cfs/test11/"
            }
        ],
        "RequestId": "adf187c6-a557-4331-b103-dded23e9bfeb",
        "TotalCount": 5
    }
}
```

