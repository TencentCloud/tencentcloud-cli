**Example 1: ModifyConfigs**

修改配置

Input: 

```
tccli tchousex ModifyConfigs --cli-unfold-argument  \
    --InstanceId abc \
    --Remark abc \
    --Component abc \
    --ModifyConfContext.0.FileName abc \
    --ModifyConfContext.0.FilePath abc \
    --ModifyConfContext.0.OldConfValue abc \
    --ModifyConfContext.0.NewConfValue abc \
    --VirtualCluster abc
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

