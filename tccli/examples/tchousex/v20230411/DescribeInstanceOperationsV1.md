**Example 1: DescribeInstanceOperationsV1**

查询集群的操作记录

Input: 

```
tccli tchousex DescribeInstanceOperationsV1 --cli-unfold-argument  \
    --InstanceId abc \
    --Offset 0 \
    --Limit 0 \
    --StartTime abc \
    --EndTime abc \
    --OperateUin abc \
    --OperateTimeOrder abc \
    --OperateObject abc \
    --State abc \
    --ExecuteTimeOrder abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "TotalCount": 0,
        "Operations": [
            {
                "InstanceId": "abc",
                "OperateUin": "abc",
                "OperateTime": "abc",
                "OperateObject": "abc",
                "OperateName": "abc",
                "State": "abc",
                "ExecuteTime": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

