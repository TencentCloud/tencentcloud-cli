**Example 1: 获取资源关联作业信息**



Input: 

```
tccli oceanus DescribeResourceRelatedJobs --cli-unfold-argument  \
    --ResourceId xx \
    --Offset 0 \
    --Limit 0 \
    --DESCByJobConfigCreateTime 0 \
    --ResourceConfigVersion 1
```

Output: 
```
{
    "Response": {
        "RefJobInfos": [
            {
                "JobConfigVersion": 0,
                "ResourceVersion": 0,
                "JobId": "xx"
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

