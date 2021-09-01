**Example 1: 查询克隆列表**



Input: 

```
tccli cdb DescribeCloneList --cli-unfold-argument  \
    --InstanceId cdb-9303wd4x
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "Items": [
            {
                "CloneJobId": 80,
                "DstInstanceId": "cdb-9ubfzt6x",
                "EndTime": "",
                "RollbackStrategy": "timepoint",
                "RollbackTargetTime": "2019-11-15 12:34:56",
                "SrcInstanceId": "cdb-4bblpca3",
                "StartTime": "2019-12-26 18:05:42",
                "TaskStatus": "initial"
            },
            {
                "CloneJobId": 81,
                "DstInstanceId": "cdb-awbsatzq",
                "EndTime": "",
                "RollbackStrategy": "backupset",
                "RollbackTargetTime": "2019-11-15 16:13:31",
                "SrcInstanceId": "cdb-4bblpca3",
                "StartTime": "2019-12-26 17:16:58",
                "TaskStatus": "initial"
            }
        ],
        "TotalCount": 2
    }
}
```

