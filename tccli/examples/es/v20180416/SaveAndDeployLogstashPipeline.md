**Example 1: 保存并部署管道**



Input: 

```
tccli es SaveAndDeployLogstashPipeline --cli-unfold-argument  \
    --InstanceId ls-xxxxxxxx \
    --Pipeline.PipelineId test \
    --Pipeline.PipelineDesc test \
    --Pipeline.Config "" \
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

