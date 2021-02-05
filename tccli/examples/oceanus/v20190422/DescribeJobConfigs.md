**Example 1: 查询作业配置列表示例**



Input: 

```
tccli oceanus DescribeJobConfigs --cli-unfold-argument  \
    --JobId cql-fktse6bt \
    --JobConfigVersions 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "JobConfigSet": [
            {
                "JobId": "cql-fktse6bt",
                "EntrypointClass": "",
                "ProgramArgs": "",
                "DefaultParallelism": 2,
                "Version": 1,
                "CreateTime": "2019-06-05 15:05:50",
                "Remark": "",
                "Properties": []
            }
        ],
        "RequestId": "5d5a201f-0a3d-485f-a82f-3c73ccca348a"
    }
}
```

