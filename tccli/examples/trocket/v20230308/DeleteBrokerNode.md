**Example 1: Broker节点剔除**

AZ故障，调用进行Broker节点剔除

Input: 

```
tccli trocket DeleteBrokerNode --cli-unfold-argument  \
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

