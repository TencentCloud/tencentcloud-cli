**Example 1: 修改共享集群标签**

修改共享集群标签

Input: 

```
tccli trocket ModifyBrokerCluster --cli-unfold-argument  \
    --ClusterName rmqbroker-cd-room1 \
    --Labels.0.Key k1 \
    --Labels.0.Value v1
```

Output: 
```
{
    "RequestId": "92bbe0de-c3de-44e3-9b10-2e5f6edba7e4",
    "Response": {
        "RequestId": "92bbe0de-c3de-44e3-9b10-2e5f6edba7e4"
    }
}
```

