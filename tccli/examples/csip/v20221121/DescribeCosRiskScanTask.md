**Example 1: 查看存储桶扫描任务详情**



Input: 

```
tccli csip DescribeCosRiskScanTask --cli-unfold-argument  \
    --BucketInfoSet.0.AppId 134567888 \
    --BucketInfoSet.0.BucketName brain-134525356
```

Output: 
```
{
    "Response": {
        "BucketTaskInfoSet": [
            {
                "AppId": 134567888,
                "BucketName": "brain-134525356",
                "TaskId": "task-1qazsxsw"
            }
        ],
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

