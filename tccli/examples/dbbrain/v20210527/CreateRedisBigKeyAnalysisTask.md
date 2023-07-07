**Example 1: 创建redis实例即时大key分析任务**

创建redis实例即时大key分析任务。

Input: 

```
tccli dbbrain CreateRedisBigKeyAnalysisTask --cli-unfold-argument  \
    --InstanceId cdb-test \
    --Product redis
```

Output: 
```
{
    "Response": {
        "RequestId": "24665720-8c93-11eb-bee6-e98cea0e6794",
        "AsyncRequestId": 8011
    }
}
```

