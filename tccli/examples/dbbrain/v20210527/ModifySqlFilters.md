**Example 1: 修改SQL限流任务状态**

修改SQL限流任务状态

Input: 

```
tccli dbbrain ModifySqlFilters --cli-unfold-argument  \
    --InstanceId cdb-test \
    --FilterIds 1433288 \
    --Status TERMINATED
```

Output: 
```
{
    "Response": {
        "RequestId": "b49053b9-f21c-40ec-a1ce-d1a5fae5193f"
    }
}
```

