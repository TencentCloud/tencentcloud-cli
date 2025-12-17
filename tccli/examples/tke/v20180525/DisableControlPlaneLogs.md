**Example 1: 删除插件日志采集配置**

删除插件日志采集配置时调用

Input: 

```
tccli tke DisableControlPlaneLogs --cli-unfold-argument  \
    --ClusterId cls-kaftesta \
    --ClusterType tke \
    --ComponentNames karpenter \
    --DeleteLogSetAndTopic False
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

