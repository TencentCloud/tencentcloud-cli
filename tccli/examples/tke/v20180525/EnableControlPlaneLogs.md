**Example 1: 创建插件日志采集配置**

创建插件日志采集配置时调用

Input: 

```
tccli tke EnableControlPlaneLogs --cli-unfold-argument  \
    --ClusterId cls-kaftesta \
    --ClusterType tke \
    --Components.0.LogLevel 2 \
    --Components.0.LogSetId 2912eb16-a56c-4b9b-adb0-9828db1ad342 \
    --Components.0.Name kube-scheduler \
    --Components.0.TopicId 2912eb16-a56c-4b9b-adb0-9828db1ad342 \
    --Components.0.TopicRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

