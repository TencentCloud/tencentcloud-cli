**Example 1: 修改一致性校验任务名称**



Input: 

```
tccli dts ModifySyncCompareTaskName --cli-unfold-argument  \
    --JobId sync-8yv4w2i1 \
    --CompareTaskId sync-8yv4w2i1-cmp-37skmii9 \
    --TaskName 对比测试
```

Output: 
```
{
    "Response": {
        "RequestId": "ac300ff0-00f2-11ed-b005-4930e69d89c2"
    }
}
```

