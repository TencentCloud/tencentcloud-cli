**Example 1: 修改serverless策略**

修改serverless策略

Input: 

```
tccli cynosdb ModifyServerlessStrategy --cli-unfold-argument  \
    --AutoPause no \
    --AutoScaleUpDelay 200 \
    --AutoPauseDelay 100 \
    --MinCpu 0.25 \
    --MaxCpu 2 \
    --ClusterId cynosdbmysql-8vcxoq75 \
    --AutoScaleDownDelay 300
```

Output: 
```
{
    "Response": {
        "FlowId": 1008300,
        "RequestId": "c3da7958-23e8-11eb-8e52-525400b7dd5a"
    }
}
```

**Example 2: 变更serverless策略**

调整主节点

Input: 

```
tccli cynosdb ModifyServerlessStrategy --cli-unfold-argument  \
    --ClusterId cynosdbmysql-92oecwyv \
    --MinCpu 2 \
    --MaxCpu 2
```

Output: 
```
{
    "Response": {
        "FlowId": 917319,
        "RequestId": "a7ef1e81-e306-45fd-ab3d-37a6ae7ecf96"
    }
}
```

