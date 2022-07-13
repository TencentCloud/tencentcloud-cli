**Example 1: 获取Logstash实例管道列表**



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
                "PipelineDesc": "1111",
                "Config": "xx",
                "Status": -2,
                "Workers": 11,
                "BatchSize": 1111,
                "BatchDelay": 111,
                "QueueType": "memory",
                "QueueMaxBytes": "1111MB",
                "QueueCheckPointWrites": 1111
            },
            {
                "PipelineId": "g4cqkhhr_2",
                "PipelineDesc": "1111",
                "Config": "xxx",
                "Status": 2,
                "Workers": 11,
                "BatchSize": 1111,
                "BatchDelay": 111,
                "QueueType": "memory",
                "QueueMaxBytes": "1111MB",
                "QueueCheckPointWrites": 1111
            }
        ],
        "RequestId": ""
    }
}
```

