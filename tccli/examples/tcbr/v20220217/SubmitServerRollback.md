**Example 1: 回滚版本**



Input: 

```
tccli tcbr SubmitServerRollback --cli-unfold-argument  \
    --EnvId abc \
    --ServerName abc \
    --CurrentVersionName abc \
    --RollbackVersionName abc \
    --OperatorRemark abc
```

Output: 
```
{
    "Response": {
        "TaskId": 0,
        "RequestId": "abc"
    }
}
```

