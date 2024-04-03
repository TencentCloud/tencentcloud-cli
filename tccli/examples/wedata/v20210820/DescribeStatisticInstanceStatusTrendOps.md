**Example 1: 1**

1

Input: 

```
tccli wedata DescribeStatisticInstanceStatusTrendOps --cli-unfold-argument  \
    --ProjectId  \
    --TaskTypeId  \
    --TimeType  \
    --TypeName  \
    --StartTime  \
    --EndTime  \
    --ExecutionGroupId  \
    --ExecutionGroupName  \
    --InCharge  \
    --AggregationUnit 
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "bf089177-0858-4917-aaa1-155ddb7accfc"
    }
}
```

**Example 2: demo**

测试

Input: 

```
tccli wedata DescribeStatisticInstanceStatusTrendOps --cli-unfold-argument  \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CountList": [
                    1
                ],
                "TimeList": [
                    "abc"
                ],
                "InstanceStatus": "abc",
                "InstanceCount": 1,
                "ShowTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 3: 后台错误**

后台错误

Input: 

```
tccli wedata DescribeStatisticInstanceStatusTrendOps --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskTypeId  \
    --StartTime 2023-12-14 00:00:00 \
    --InCharge  \
    --StateList 2 \
    --AggregationUnit H
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "实例状态趋势获取异常:[500] during [GET] to [http://scheduler-gateway-service/api/taskScheduler/instanceStatusReport/instanceTrend?projectId=1460947878944567296&inCharge&stateList=2&startTime=2023-12-14%2000%3A00%3A00&aggregationUnit=H] [ScheduleOpsApi#countByType(String,String,Integer,List,String,String,String,Integer)]: [{\"timestamp\":\"2023-12-15T02:47:53.694+00:00\",\"status\":500,\"error\":\"Internal Server Error\",\"path\":\"/api/taskScheduler/instanceStatusReport/instanceTrend\"}]"
        },
        "RequestId": "1a450423-a41a-44b0-83dd-e53ebc215862"
    }
}
```

