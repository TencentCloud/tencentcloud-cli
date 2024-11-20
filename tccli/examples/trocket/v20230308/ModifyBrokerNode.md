**Example 1: CSM故障调度Broker节点加回**

AZ故障恢复后，用于加回Broker节点

Input: 

```
tccli trocket ModifyBrokerNode --cli-unfold-argument  \
    --InstanceId rocket-vip-basic-1 \
    --ZoneId 10001
```

Output: 
```
{
    "Response": {
        "TaskId": "4ed3a07b-36ef-4522-968b-5434dff663da",
        "RequestId": "abc"
    }
}
```

