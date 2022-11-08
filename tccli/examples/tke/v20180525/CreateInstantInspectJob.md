**Example 1: 调用api创建TKE集群巡检任务**



Input: 

```
tccli tke CreateInstantInspectJob --cli-unfold-argument  \
    --ClusterId cls-test
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "JobName": "job-test"
    }
}
```

