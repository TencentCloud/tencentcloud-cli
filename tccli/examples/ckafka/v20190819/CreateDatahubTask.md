**Example 1: 创建SINK任务**

SINK任务

Input: 

```
tccli ckafka CreateDatahubTask --cli-unfold-argument  \
    --TaskName MyTaskName \
    --TaskType SINK \
    --SourceResource.Type KAFKA \
    --SourceResource.KafkaParam.SelfBuilt False \
    --SourceResource.KafkaParam.Resource ckafka-7kd5rzza \
    --SourceResource.KafkaParam.Topic topic-test \
    --SourceResource.KafkaParam.OffsetType timestamp \
    --SourceResource.KafkaParam.StartTime 1635339533 \
    --TargetResource.Type EB \
    --TargetResource.EventBusParam.Type COS \
    --TargetResource.EventBusParam.SelfBuilt False \
    --TargetResource.EventBusParam.Resource target-resource \
    --TargetResource.EventBusParam.Namespace default \
    --TargetResource.EventBusParam.FunctionName ckafka-7kd5rzza_topic-0cus2p9z_task_1633501781881_schedule \
    --TargetResource.EventBusParam.Qualifier $LATEST
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "datahub-xx",
            "DatahubId": "xx"
        },
        "RequestId": "xx"
    }
}
```

**Example 2: 创建SINK任务(ES)**



Input: 

```
tccli ckafka CreateDatahubTask --cli-unfold-argument  \
    --TaskName MyTaskName \
    --TaskType SINK \
    --SourceResource.Type KAFKA \
    --SourceResource.KafkaParam.SelfBuilt False \
    --SourceResource.KafkaParam.Resource ckafka-7kd5rzza \
    --SourceResource.KafkaParam.Topic topic-test \
    --SourceResource.KafkaParam.OffsetType earliest \
    --TargetResource.Type ES \
    --TargetResource.EsParam.Resource resource-xxx \
    --TargetResource.EsParam.DropInvalidMessage True \
    --TargetResource.EsParam.Index xxx \
    --TargetResource.EsParam.DropInvalidJsonMessage False
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "task-xx",
            "DatahubId": "xx"
        },
        "RequestId": "xx"
    }
}
```

**Example 3: 创建TRANSFORM任务**

TRANSFORM任务

Input: 

```
tccli ckafka CreateDatahubTask --cli-unfold-argument  \
    --TaskName MyTaskName \
    --TaskType TRANSFORM \
    --SourceResource.Type KAFKA \
    --SourceResource.KafkaParam.SelfBuilt False \
    --SourceResource.KafkaParam.Resource ckafka-aaa \
    --SourceResource.KafkaParam.Topic topic-source \
    --TargetResource.Type KAFKA \
    --TargetResource.KafkaParam.SelfBuilt False \
    --TargetResource.KafkaParam.Resource ckafka-bbb \
    --TargetResource.KafkaParam.Topic topic-traget \
    --TransformParam.Regex ; \
    --TransformParam.AnalysisFormat DELIMITER \
    --TransformParam.OutputFormat JSON \
    --TransformParam.SourceType xx \
    --TransformParam.FilterParam.0.MatchMode PREFIX \
    --TransformParam.FilterParam.0.Value cass \
    --TransformParam.FilterParam.0.Key 0 \
    --TransformParam.FailureParam.Type DLQ \
    --TransformParam.FailureParam.MaxRetryAttempts 1 \
    --TransformParam.FailureParam.KafkaParam.Resource ckafka-xxx \
    --TransformParam.FailureParam.KafkaParam.SelfBuilt False \
    --TransformParam.FailureParam.KafkaParam.Topic test-dlq \
    --TransformParam.Content xx \
    --TransformParam.MapParam.0.Type DEFAULT \
    --TransformParam.MapParam.0.Key 1 \
    --TransformParam.MapParam.1.Type DEFAULT \
    --TransformParam.MapParam.1.Key 2 \
    --TransformParam.MapParam.2.Type DEFAULT \
    --TransformParam.MapParam.2.Value abc \
    --TransformParam.MapParam.2.Key 3 \
    --TransformParam.MapParam.3.Type DATE \
    --TransformParam.MapParam.3.Value  \
    --TransformParam.MapParam.3.Key 5
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "datahub-xx",
            "DatahubId": "xx"
        },
        "RequestId": "xx"
    }
}
```

**Example 4: 创建SINK任务(DIP Topic to ES)**



Input: 

```
tccli ckafka CreateDatahubTask --cli-unfold-argument  \
    --TaskName MyTaskName \
    --TaskType SINK \
    --SourceResource.Type TOPIC \
    --SourceResource.TopicParam.Resource 12345-xxx \
    --SourceResource.TopicParam.OffsetType earliest \
    --TargetResource.Type ES \
    --TargetResource.EsParam.Resource resource-xxx \
    --TargetResource.EsParam.DropInvalidMessage True \
    --TargetResource.EsParam.Index xxx \
    --TargetResource.EsParam.DropInvalidJsonMessage False
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "task-xx",
            "DatahubId": "xx"
        },
        "RequestId": "xx"
    }
}
```

