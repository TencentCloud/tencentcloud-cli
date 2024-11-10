**Example 1: 提交实例升级检查任务**

无

Input: 

```
tccli cdb SubmitInstanceUpgradeCheckJob --cli-unfold-argument  \
    --InstanceId cdb-g3rbtabc \
    --DstMysqlVersion 8.0
```

Output: 
```
{
    "Response": {
        "JobId": 145,
        "RequestId": "a4b54232-d7af-4df3-8329-5110e3ece9c3"
    }
}
```

