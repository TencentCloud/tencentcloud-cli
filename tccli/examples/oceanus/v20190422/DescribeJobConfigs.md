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
        "RequestId": "xx",
        "JobConfigSet": [
            {
                "ProgramArgs": "xx",
                "Remark": "xx",
                "CreatorUin": "xx",
                "DefaultParallelism": 1,
                "ResourceRefDetails": [
                    {
                        "ResourceId": "xx",
                        "SystemProvide": 0,
                        "Type": 0,
                        "Version": 0,
                        "Name": "xx"
                    }
                ],
                "COSBucket": "xx",
                "UpdateTime": "xx",
                "JobId": "xx",
                "EntrypointClass": "xx",
                "Version": 1,
                "Properties": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "LogCollect": 0,
                "MaxParallelism": 1,
                "CreateTime": "xx"
            }
        ]
    }
}
```

