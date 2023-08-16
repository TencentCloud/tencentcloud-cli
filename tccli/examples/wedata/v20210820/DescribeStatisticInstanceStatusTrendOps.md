**Example 1: demo**

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

**Example 2: 1**

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

