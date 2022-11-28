**Example 1: 修改集群配置文件接口**

在集群配置页面修改集群配置文件接口，xml模式

Input: 

```
tccli cdwch ModifyClusterConfigs --cli-unfold-argument  \
    --InstanceId cdwch-xxxx \
    --ModifyConfContext.0.FileName xxxx \
    --ModifyConfContext.0.OldConfValue xxxxx \
    --ModifyConfContext.0.NewConfValue xxxx \
    --Remark xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx",
        "FlowId": 0,
        "ErrorMsg": ""
    }
}
```

