**Example 1: 查看cos对象存储扫描任务**



Input: 

```
tccli csip DescribeCosObjectScanTask --cli-unfold-argument  \
    --TaskType 2 \
    --MemberId mem-a6df317cb6a8c424 \
    --BucketSet 0313-vtanakwang-260082268
```

Output: 
```
{
    "Response": {
        "MemberTaskIdSet": [
            {
                "AppId": 251002343,
                "LastScanTime": 0,
                "TaskId": ""
            }
        ],
        "RequestId": "daea542d-c4a7-48ca-84a2-4e4e255b29c6"
    }
}
```

