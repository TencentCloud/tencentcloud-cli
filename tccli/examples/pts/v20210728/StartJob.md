**Example 1: 创建并启动任务**

创建并启动任务

Input: 

```
tccli pts StartJob --cli-unfold-argument  \
    --ProjectId project-xx \
    --JobOwner xiaohong \
    --ScenarioId scenario-xx
```

Output: 
```
{
    "Response": {
        "RequestId": "req-xx",
        "JobId": "job-xx"
    }
}
```

