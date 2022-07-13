**Example 1: 删除Logstash管道**



Input: 

```
tccli es DeleteLogstashPipelines --cli-unfold-argument  \
    --InstanceId ls-xxxxxxxx \
    --PipelineIds test
```

Output: 
```
{
    "Response": {
        "RequestId": "6eb5c3b2-0bba-4f73-bafb-bd21esxxxxxx"
    }
}
```

