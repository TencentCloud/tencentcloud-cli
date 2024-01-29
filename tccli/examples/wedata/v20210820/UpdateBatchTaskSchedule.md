**Example 1: 失败**

失败

Input: 

```
tccli wedata UpdateBatchTaskSchedule --cli-unfold-argument  \
    --TaskIds abc \
    --SelfDepend abc \
    --StartTime abc \
    --EndTime abc \
    --DelayTime 0 \
    --TaskAction abc \
    --CycleType abc \
    --CycleStep 0 \
    --CrontabExpression abc \
    --ExecutionStartTime abc \
    --ExecutionEndTime abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 失败2**

失败2

Input: 

```
tccli wedata UpdateBatchTaskSchedule --cli-unfold-argument  \
    --TaskIds 20230608210301228 \
    --SelfDepend serial \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "Connect to 30.181.47.125:49222 [/30.181.47.125] failed: Connection refused (Connection refused) executing POST http://platformgateway/cloudapi/platformgateway/v1/platform/DescribeUserName"
        },
        "RequestId": "3f96b805-605f-4fa5-8ed5-a012d084c313"
    }
}
```

**Example 3: 失败3**

失败3

Input: 

```
tccli wedata UpdateBatchTaskSchedule --cli-unfold-argument  \
    --TaskIds 20230608210301228 \
    --SelfDepend parallel \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "47ab5f39-eb46-40c5-ad09-f41b5b67b819"
    }
}
```

**Example 4: 成功**



Input: 

```
tccli wedata UpdateBatchTaskSchedule --cli-unfold-argument  \
    --TaskIds abc \
    --SelfDepend abc \
    --StartTime abc \
    --EndTime abc \
    --DelayTime 0 \
    --TaskAction abc \
    --CycleType abc \
    --CycleStep 0 \
    --CrontabExpression abc \
    --ExecutionStartTime abc \
    --ExecutionEndTime abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 5: 成功3**

成功3

Input: 

```
tccli wedata UpdateBatchTaskSchedule --cli-unfold-argument  \
    --TaskIds 20230718165938743 \
    --SelfDepend serial \
    --StartTime 2023-08-09 00:00:00 \
    --EndTime 2023-08-10 23:59:59 \
    --DelayTime 0 \
    --TaskAction  \
    --CycleType HOUR_CYCLE \
    --CycleStep 1 \
    --CrontabExpression 0 0 0-23/1 * * ? \
    --ExecutionStartTime 0:00 \
    --ExecutionEndTime 23:59 \
    --ProjectId 1470561602745229312
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

