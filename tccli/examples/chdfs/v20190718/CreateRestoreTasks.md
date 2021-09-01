**Example 1: 批量创建回热任务**

批量创建回热任务

Input: 

```
tccli chdfs CreateRestoreTasks --cli-unfold-argument  \
    --FileSystemId f4mhaqkciq0 \
    --RestoreTasks.0.FilePath /test/file2 \
    --RestoreTasks.0.Type 2 \
    --LifeCycleRules.0.Days 7
```

Output: 
```
{
    "Response": {
        "RequestId": "5d6d3ef8-db1d-40de-afa1-d340302458bb"
    }
}
```

