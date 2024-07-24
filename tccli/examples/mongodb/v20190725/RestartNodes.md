**Example 1: 重启Mongod节点**



Input: 

```
tccli mongodb RestartNodes --cli-unfold-argument  \
    --InstanceId cmgo-pvwp23v1 \
    --NodeIds cmgo-pvwp23v1_0-node-slave0 cmgo-pvwp23v1_0-node-slave1
```

Output: 
```
{
    "Response": {
        "RequestId": "2efcf780-9970-11ec-8975-6bc44e3bfad7",
        "FlowId": 19677
    }
}
```

