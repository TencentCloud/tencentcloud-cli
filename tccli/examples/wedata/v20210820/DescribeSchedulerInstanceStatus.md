**Example 1: 示例1**

实例状态分布

Input: 

```
tccli wedata DescribeSchedulerInstanceStatus --cli-unfold-argument  \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CountTag": 1,
                "TotalNum": 1,
                "RunningNum": 1,
                "WaitRunningNum": 1,
                "DependencyNum": 1,
                "WaitEventNum": "abc",
                "StoppingNum": 1,
                "SucceedNum": 1,
                "FailedNum": 1
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
tccli wedata DescribeSchedulerInstanceStatus --cli-unfold-argument  \
    --ProjectId abc \
    --TaskTypeId abc \
    --ExecutionGroupId abc \
    --ExecutionGroupName abc \
    --StartTime abc \
    --EndTime abc \
    --InCharge abc
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "72dd1900-2555-4298-89a4-680fb1c3993c"
    }
}
```

**Example 3: 测试**

测试

Input: 

```
tccli wedata DescribeSchedulerInstanceStatus --cli-unfold-argument  \
    --ProjectId 1470561602745229312 \
    --StartTime 2023-07-30 23:59:59
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "The provided credentials could not be validated. Please check your signature is correct."
        },
        "RequestId": "dc00c9b3-faec-404b-a2da-da2653ba026b"
    }
}
```

