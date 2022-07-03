**Example 1: 隔离实例访问**



Input: 

```
tccli cynosdb IsolateInstance --cli-unfold-argument  \
    --InstanceIdList cynosdbmysql-ixgbd0di \
    --ClusterId cynosdbmysql-ins-bzkxxrmt
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "DealNames": [
            "23456"
        ],
        "FlowId": "123"
    }
}
```

