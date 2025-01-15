**Example 1: 修改集群配置文件接口**

在集群配置页面修改集群配置文件接口，xml模式

Input: 

```
tccli cdwdoris ModifyClusterConfigs --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3 \
    --ModifyConfContext.0.FileName be.conf \
    --ModifyConfContext.0.OldConfValue 31234 \
    --ModifyConfContext.0.NewConfValue 2123 \
    --Remark addconf
```

Output: 
```
{
    "Response": {
        "RequestId": "dasfwer2341231-123sadwq42",
        "FlowId": 0,
        "ErrorMsg": ""
    }
}
```

