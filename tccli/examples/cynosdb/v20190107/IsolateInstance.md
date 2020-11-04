**Example 1: 隔离实例访问**



Input: 

```
tccli cynosdb IsolateInstance --cli-unfold-argument  \
    --ClusterId cynosdbpg-ins-bzkxxrmt\
    --InstanceIdList cynosdbpg-ixgbd0di
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": "123"
    }
}
```

