**Example 1: 续跑执行失败的任务批次**



Input: 

```
tccli tsf ContinueRunFailedTaskBatch --cli-unfold-argument  \
    --BatchId batch-12345678
```

Output: 
```
{
    "Response": {
        "Result": true
    }
}
```

