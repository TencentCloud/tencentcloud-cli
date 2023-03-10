**Example 1: 查询克隆列表**

查询克隆列表

Input: 

```
tccli cdb DescribeCloneList --cli-unfold-argument  \
    --InstanceId cdb-9303wd4x
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "Items": [
            {
                "SrcInstanceId": "cdb-4bblpca3",
                "RollbackTargetTime": "2019-11-15 12:34:56",
                "CloneJobId": 80,
                "SrcRegionId": 0,
                "TaskStatus": "initial",
                "NewRegionId": 8,
                "RollbackStrategy": "test",
                "StartTime": "2019-12-26 18:05:42",
                "DstInstanceId": "cdb-9ubfzt6x",
                "EndTime": ""
            },
            {
                "SrcInstanceId": "cdb-4bblpca3",
                "RollbackTargetTime": "2019-11-15 16:13:31",
                "CloneJobId": 81,
                "SrcRegionId": 4,
                "TaskStatus": "initial",
                "StartTime": "2019-12-26 17:16:58",
                "RollbackStrategy": "backupset",
                "NewRegionId": 0,
                "DstInstanceId": "cdb-awbsatzq",
                "EndTime": ""
            }
        ]
    }
}
```

