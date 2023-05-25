**Example 1: 修改实例参数**



Input: 

```
tccli cynosdb ModifyInstanceParam --cli-unfold-argument  \
    --InstanceParamList.0.CurrentValue 2 \
    --InstanceParamList.0.ParamName innodb_stats_transient_sample_pages \
    --ClusterId cynosdbmysql-ge5ck0jr \
    --InstanceIds cynosdbmysql-ins-kzavkukw \
    --IsInMaintainPeriod no
```

Output: 
```
{
    "Response": {
        "FlowId": 1103611,
        "RequestId": "77735431-2058-4999-ace4-a16874c2177b"
    }
}
```

