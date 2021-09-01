**Example 1: 调用成功示例**



Input: 

```
tccli iai GetCheckSimilarPersonJobIdList --cli-unfold-argument  \
    --Limit 2 \
    --Version 2018-03-01
```

Output: 
```
{
    "Response": {
        "JobIdInfos": [
            {
                "JobId": "d6dGLOcFSISPtIfy",
                "StartTime": 1576567050654,
                "JobStatus": 0
            },
            {
                "JobId": "251006443_merge_person_1576565489_wjBy9I3B",
                "StartTime": 1576565489239,
                "JobStatus": 2
            }
        ],
        "JobIdNum": 408,
        "RequestId": "6434816c-3b15-4f26-b909-8f5a8452cd58"
    }
}
```

**Example 2: 调用失败示例**



Input: 

```
tccli iai GetCheckSimilarPersonJobIdList --cli-unfold-argument  \
    --Limit 1001 \
    --Version 2018-03-01
```

Output: 
```
{
    "Response": {
        "RequestId": "3bc56633-5efd-4cff-8dfb-08ac6f88a8b9"
    }
}
```

