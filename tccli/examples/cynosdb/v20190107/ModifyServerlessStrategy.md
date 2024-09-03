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

