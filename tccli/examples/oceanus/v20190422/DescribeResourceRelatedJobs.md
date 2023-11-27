**Example 1: 查询依赖关联作业**

查询特定关联作业

Input: 

```
tccli oceanus DescribeResourceRelatedJobs --cli-unfold-argument  \
    --ResourceId resource-ew6aw29s \
    --Offset 0 \
    --Limit 100 \
    --ResourceConfigVersion 1 \
    --WorkSpaceId space-1257057943ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RefJobInfos": [
            {
                "JobConfigVersion": -1,
                "JobId": "cql-oy8hvq7i",
                "ResourceVersion": 1
            }
        ],
        "RequestId": "5c2f633d-1706-492b-811f-4cdd6ec24810",
        "TotalCount": 1
    }
}
```

