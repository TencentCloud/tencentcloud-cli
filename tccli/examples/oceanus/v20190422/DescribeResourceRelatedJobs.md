**Example 1: 正常请求【无子请求】**



Input: 

```
tccli oceanus DescribeResourceRelatedJobs --cli-unfold-argument  \
    --ResourceId xx \
    --Offset 0 \
    --Limit 0 \
    --DESCByJobConfigCreateTime 0
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

