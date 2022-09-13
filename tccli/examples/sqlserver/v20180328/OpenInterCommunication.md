**Example 1: 设置实例加入互通组**



Input: 

```
tccli sqlserver OpenInterCommunication --cli-unfold-argument  \
    --InstanceIdSet mssql-hlh6yka1 mssql-gfh54fg2
```

Output: 
```
{
    "Response": {
        "InterInstanceFlowSet": [
            {
                "FlowId": 0,
                "InstanceId": "mssql-hlh6yka1"
            },
            {
                "FlowId": 1253,
                "InstanceId": "mssql-gfh54fg2"
            }
        ],
        "RequestId": "fc3376a3-4585-4442-87cd-6076d3b510bc"
    }
}
```

