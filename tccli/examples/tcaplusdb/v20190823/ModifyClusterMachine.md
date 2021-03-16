**Example 1: 修改集群Cluster的独占机器**

修改集群Cluster的独占机器

Input: 

```
tccli tcaplusdb ModifyClusterMachine --cli-unfold-argument  \
    --ProxyList.0.MachineNum 0 \
    --ProxyList.0.MachineType T1 \
    --ServerList.0.MachineNum 0 \
    --ServerList.0.MachineType T1 \
    --ClusterId 6179109757 \
    --ClusterType 0
```

Output: 
```
{
    "Response": {
        "ClusterId": "6179109757",
        "RequestId": "8f1cc454-4a80-4ed3-a6c3-b7df2b0e8ec7"
    }
}
```

