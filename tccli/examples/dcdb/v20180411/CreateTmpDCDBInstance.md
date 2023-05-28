**Example 1: 回档TDSQL分布式数据库实例**

回档TDSQL分布式数据库实例

Input: 

```
tccli dcdb CreateTmpDCDBInstance --cli-unfold-argument  \
    --InstanceId tdsqlshard-1pif6bs0 \
    --RollbackTime 2020-01-15+10%3A27%3A02
```

Output: 
```
{
    "Response": {
        "FlowId": 1001056,
        "RequestId": "7359902f-582d-4fe0-a610-6be23bf8db48"
    }
}
```

