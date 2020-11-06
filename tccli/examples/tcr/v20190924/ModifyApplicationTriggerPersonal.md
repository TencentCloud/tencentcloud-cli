**Example 1: 修改应用更新触发器**



Input: 

```
tccli tcr ModifyApplicationTriggerPersonal --cli-unfold-argument  \
    --RepoName test/test123 \
    --TriggerName testtrig \
    --InvokeMethod all \
    --ClusterId cls-xxxxxxxx \
    --Namespace default \
    --WorkloadType Deployment \
    --WorkloadName testdeploy \
    --ContainerName nginx \
    --ClusterRegion 16 \
    --NewTriggerName test2
```

Output: 
```
{
    "Response": {
        "RequestId": "26358c69-7254-41e8-8f4e-bb13836e4165"
    }
}
```

