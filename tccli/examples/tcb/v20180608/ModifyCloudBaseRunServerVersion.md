**Example 1: 示例**



Input: 

```
tccli tcb ModifyCloudBaseRunServerVersion --cli-unfold-argument  \
    --EnvId lotestapi100004 \
    --ServerName dockerservicename \
    --VersionName dbde \
    --EnvParams dnide \
    --ContainerPort 8080 \
    --Remark test \
    --CustomLogs stdout \
    --IsResetRemark true
```

Output: 
```
{
    "Response": {
        "Result": "succ",
        "RequestId": "5620b49e-a25a-4007-84ef-03c9035c584d"
    }
}
```

