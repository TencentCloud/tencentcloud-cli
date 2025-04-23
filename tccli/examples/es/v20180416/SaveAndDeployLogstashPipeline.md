**Example 1: 保存并部署管道**



Input: 

```
tccli es SaveAndDeployLogstashPipeline --cli-unfold-argument  \
    --InstanceId ls-xxxxxxxx \
    --Pipeline.PipelineId ' pipe_xxx' \
    --Pipeline.PipelineDesc 管道描述 \
    --Pipeline.Config "aW5wdXR7CiAgICAjxxx" \
    --Pipeline.QueueCheckPointWrites 1000 \
    --Pipeline.QueueType "persisted" \
    --Pipeline.QueueMaxBytes 1GB \
    --Pipeline.BatchDelay 50 \
    --Pipeline.BatchSize 1000 \
    --Pipeline.Workers 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6eb5c3b2-0bba-4f73-bafb-bd21esxxxxxx"
    }
}
```

