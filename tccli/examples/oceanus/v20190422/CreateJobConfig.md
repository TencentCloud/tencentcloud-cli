**Example 1: 新建作业配置示例**



Input: 

```
tccli oceanus CreateJobConfig --cli-unfold-argument  \
    --JobId cql-n8yaia0y \
    --EntrypointClass com.tencent.flink.test.WordCount \
    --ProgramArgs 2000
```

Output: 
```
{
    "Response": {
        "Version": 2,
        "RequestId": "5f124d6f-b035-4d29-9467-dd62eccdbf23"
    }
}
```

