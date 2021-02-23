**Example 1: 查询异步任务执行结果**



Input: 

```
tccli ecm DescribeTaskResult --cli-unfold-argument  \
    --TaskId 1528600 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "TaskId": "1528600",
        "Result": "SUCCESS",
        "RequestId": "f2e74569-c189-4396-80ab-1482134a1e52"
    }
}
```

