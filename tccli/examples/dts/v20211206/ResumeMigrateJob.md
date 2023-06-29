**Example 1: 重试失败的数据迁移任务**

在任务失败时，以覆盖写等模式重试已经失败的数据迁移任务

Input: 

```
tccli dts ResumeMigrateJob --cli-unfold-argument  \
    --JobId dts-j7bt5sid \
    --ResumeOption normal
```

Output: 
```
{
    "Response": {
        "RequestId": "22f6b9ca-e94d-4a4d-b48f-a5133e791374"
    }
}
```

