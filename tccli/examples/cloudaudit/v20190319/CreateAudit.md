**Example 1: 创建跟踪集**

创建跟踪集

Input: 

```
tccli cloudaudit CreateAudit --cli-unfold-argument  \
    --AuditName auditTest_1 \
    --CmqQueueName cmq-01 \
    --CmqRegion sh \
    --CosBucketName cos-01 \
    --CosRegion ap-shanghai \
    --IsCreateNewBucket 1 \
    --IsCreateNewQueue 1 \
    --IsEnableCmqNotify 1 \
    --LogFilePrefix akshsb1j \
    --ReadWriteAttribute 2
```

Output: 
```
{
    "Response": {
        "IsSuccess": 1,
        "RequestId": "e9501707-784a-474c-b524-67ed9d3a6b50"
    }
}
```

