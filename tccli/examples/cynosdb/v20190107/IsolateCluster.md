**Example 1: 隔离集群**



Input: 

```
tccli cynosdb IsolateCluster --cli-unfold-argument  \
    --ClusterId cynosdbmysql-bzxxrmtq
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": "123",
        "DealNames": [
            "123"
        ]
    }
}
```

