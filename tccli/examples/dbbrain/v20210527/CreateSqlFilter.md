**Example 1: 创建实例SQL限流任务**

创建实例SQL限流任务

Input: 

```
tccli dbbrain CreateSqlFilter --cli-unfold-argument  \
    --InstanceId cdb-test \
    --SqlType SELECT \
    --FilterKey t1,t2 \
    --MaxConcurrency 1 \
    --Duration 300
```

Output: 
```
{
    "Response": {
        "FilterId": 7011,
        "RequestId": "24665720-8c93-11eb-bee6-e98cea0e6794"
    }
}
```

