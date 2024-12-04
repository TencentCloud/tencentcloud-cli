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
            "TaskId": "task-y9799wbn",
            "DatahubId": "datahub-y9799wbn"
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
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
    --TargetResource.EsParam.Resource resource-test \
    --TargetResource.EsParam.DropInvalidMessage True \
    --TargetResource.EsParam.Index index \
    --TargetResource.EsParam.DropInvalidJsonMessage False
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "task-y9799wbn",
            "DatahubId": "datahub-y9799wbn"
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```

**Example 3: 创建SINK任务(DIP Topic to ES)**



Input: 

```
tccli ckafka CreateDatahubTask --cli-unfold-argument  \
    --TaskName MyTaskName \
    --TaskType SINK \
    --SourceResource.Type TOPIC \
    --SourceResource.TopicParam.Resource 12345-xxx \
    --SourceResource.TopicParam.OffsetType earliest \
    --TargetResource.Type ES \
    --TargetResource.EsParam.Resource resource-test \
    --TargetResource.EsParam.DropInvalidMessage True \
    --TargetResource.EsParam.Index index \
    --TargetResource.EsParam.DropInvalidJsonMessage False
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "task-y9799wbn",
            "DatahubId": "datahub-y9799wbn"
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```

