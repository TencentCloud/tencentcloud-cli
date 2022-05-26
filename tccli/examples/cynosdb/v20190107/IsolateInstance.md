**Example 1: 隔离实例访问**



Input: 

```
tccli cynosdb IsolateInstance --cli-unfold-argument  \
    --ClusterId cynosdbmysql-ins-bzkxxrmt \
    --InstanceIdList cynosdbmysql-ixgbd0di
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

