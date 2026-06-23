**Example 1: 模拟节点宕机**



Input: 

```
tccli cynosdb MockNodeDown --cli-unfold-argument  \
    --ClusterId cynosdbmysql-pub24n35 \
    --InstanceId cynosdbmysql-ins-iiznk2ic \
    --SetRecoverFail False
```

Output: 
```
{
    "Response": {
        "FlowId": 1043961,
        "TaskId": 42046,
        "RequestId": "ff6e26c7-5a54-4555-9fdf-506e05e7c679"
    }
}
```

