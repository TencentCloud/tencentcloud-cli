**Example 1: 新建作业配置示例**

创建一个作业配置

Input: 

```
tccli oceanus CreateJobConfig --cli-unfold-argument  \
    --ProgramArgs 2000 \
    --EntrypointClass com.tencent.flink.test.WordCount \
    --JobId cql-n8yaia0y
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

