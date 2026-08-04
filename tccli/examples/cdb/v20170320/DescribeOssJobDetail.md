**Example 1: 查询异步任务**

查询当前异步任务已暂停

Input: 

```
tccli cdb DescribeOssJobDetail --cli-unfold-argument  \
    --InstanceId cdb-1yrgrdmr \
    --JobId 148123648
```

Output: 
```
{
    "Response": {
        "CreateTime": "2026-05-18 18:08:57",
        "Progress": 33,
        "Status": "pause",
        "StepAll": 2,
        "StepNow": 1,
        "WorkError": "",
        "WorkErrorNo": 0,
        "RequestId": "7dd44bb2-6889-44bf-bdb0-9c2573bf48df"
    }
}
```

