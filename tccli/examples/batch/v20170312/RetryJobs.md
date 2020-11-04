**Example 1: 重试作业**

任务中出现部分实例失败时，仅重试失败的任务实例，已成功的任务不作处理。

Input: 

```
tccli batch RetryJobs --cli-unfold-argument  \
    --JobIds job-rybewp57 job-97zcl3wt
```

Output: 
```
{
    "Response": {
        "RequestId": "970e5a9f-2963-436c-8dad-4847360676f7"
    }
}
```

