**Example 1: 批量运行任务**

任务运维-批量运行任务

Input: 

```
tccli wedata BatchRunOpsTask --cli-unfold-argument  \
    --ProjectId abc \
    --EnableMakeUp 0 \
    --Tasks abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

