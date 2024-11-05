**Example 1: 隔离专业集群一个可用区**

隔离专业集群一个可用区

Input: 

```
tccli tdmq IsolatePulsarClusterZone --cli-unfold-argument  \
    --ClusterId pulsar-a827x2daroad \
    --Zones ap-chengdu-2 \
    --ActionType isolate
```

Output: 
```
{
    "Response": {
        "TaskId": "4c2e555d-ea63-47b2-804d-fcb4f3869f73",
        "RequestId": "4c2e555d-ea63-47b2-804d-fcb4f386234f"
    }
}
```

