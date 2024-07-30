**Example 1: 修改集群配置接口**

在集群配置页面修改集群接口

Input: 

```
tccli cdwdoris FitClsLog --cli-unfold-argument  \
    --InstanceId cdwch-xxxx \
    --ClsLogSetId xxxx
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

