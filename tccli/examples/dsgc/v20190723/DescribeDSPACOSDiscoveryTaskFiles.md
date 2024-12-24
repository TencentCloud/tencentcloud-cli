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
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

