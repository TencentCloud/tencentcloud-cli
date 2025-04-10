**Example 1: 获取Logstash实例管道列表**

获取Logstash实例管道列表

Input: 

```
tccli es DescribeLogstashPipelines --cli-unfold-argument  \
    --InstanceId ls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "LogstashPipelineList": [
            {
                "PipelineId": "g4cqkhhr_1",
                "PipelineDesc": "企业基本信息",
                "Config": "input{\n    # xxx}",
                "Status": -2,
                "Workers": 11,
                "BatchSize": 1111,
                "BatchDelay": 111,
                "QueueType": "memory",
                "QueueMaxBytes": "1111MB",
                "QueueCheckPointWrites": 1111,
                "CreateTime": "2023-12-14 11:09:32",
                "UpdateTime": "2023-12-14 11:15:44"
            },
            {
                "PipelineId": "g4cqkhhr_2",
                "PipelineDesc": "企业",
                "Config": "input{xxx}",
                "Status": 2,
                "Workers": 11,
                "BatchSize": 1111,
                "BatchDelay": 111,
                "QueueType": "memory",
                "QueueMaxBytes": "1111MB",
                "QueueCheckPointWrites": 1111,
                "CreateTime": "2023-12-14 11:09:32",
                "UpdateTime": "2023-12-14 11:15:44"
            }
        ],
        "RequestId": ""
    }
}
```

