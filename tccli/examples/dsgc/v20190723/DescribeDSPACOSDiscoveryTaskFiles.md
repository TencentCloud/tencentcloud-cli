**Example 1: 获取COS分类分级任务结果详情文件列表**



Input: 

```
tccli dsgc DescribeDSPACOSDiscoveryTaskFiles --cli-unfold-argument  \
    --DspaId dspa-001 \
    --BucketResultId 123 \
    --TaskId 123
```

Output: 
```
{
    "Response": {
        "Files": [
            "file_1",
            "file_2"
        ],
        "RequestId": "xx"
    }
}
```

