**Example 1: DescribeInstanceOperations**

获取集群操作信息

Input: 

```
tccli tchousex DescribeInstanceOperations --cli-unfold-argument  \
    --InstanceId abc \
    --Offset 0 \
    --Limit 0 \
    --StartTime abc \
    --EndTime abc \
    --VirtualCluster abc \
    --OperatorAppid 0 \
    --OperatorUin abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Operations": [
            {
                "Id": 0,
                "InstanceId": "abc",
                "VirtualCluster": "abc",
                "Action": "abc",
                "Status": 0,
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "EndTime": "abc",
                "Context": "abc",
                "OperatorAppid": 0,
                "OperatorUin": "abc"
            }
        ],
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

