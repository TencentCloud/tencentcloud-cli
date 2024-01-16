**Example 1: 1**

1

Input: 

```
tccli wedata DescribeTaskByStatusReport --cli-unfold-argument  \
    --Type  \
    --TaskType  \
    --TypeName  \
    --ProjectId  \
    --StartTime  \
    --EndTime  \
    --AggregationUnit 
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnknownParameter",
            "Message": "The parameter `AggregationUnit` is not recognized."
        },
        "RequestId": "7198e47e-2532-4f81-9bfa-790451eb1723"
    }
}
```

**Example 2: 2**

2

Input: 

```
tccli wedata DescribeTaskByStatusReport --cli-unfold-argument  \
    --Type  \
    --TaskType  \
    --TypeName  \
    --ProjectId  \
    --StartTime  \
    --EndTime  \
    --AggregationUnit  \
    --CycleUnit  \
    --Status  \
    --InCharge 
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "fcbfd6fb-66a2-43be-bbe3-ab579806ff0e"
    }
}
```

**Example 3: 后台错误**

后台错误

Input: 

```
tccli wedata DescribeTaskByStatusReport --cli-unfold-argument  \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "任务状态趋势异常:[400] during [GET] to [http://scheduler-gateway-service/api/taskScheduler/taskStatusReport/taskStatusTrend?projectId=1460947878944567296] [ScheduleOpsApi#taskStatusTrend(String,String,Integer,String,String,String,String,String)]: [{\"timestamp\":\"2023-12-15T02:51:24.240+00:00\",\"status\":400,\"error\":\"Bad Request\",\"path\":\"/api/taskScheduler/taskStatusReport/taskStatusTrend\"}]"
        },
        "RequestId": "63e6dac5-742d-422d-aa90-dbb0e9ce666d"
    }
}
```

