**Example 1: 获取实例操作日志纪录**

指定实例ID后获取实例的操作日志纪录

Input: 

```
tccli emr DescribeInstanceOplog --cli-unfold-argument  \
    --InstanceId emr-0sfuq468 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "LogList": [
            {
                "CreateTime": "2020-02-19 20:58:11",
                "InstanceId": 59763,
                "Operand": "集群",
                "Operation": "创建集群",
                "OperationDesc": "---",
                "OperationType": 1,
                "Operator": "1875765535",
                "SecurityLevel": "一般",
                "UserType": 1
            }
        ],
        "RequestId": "d7f5f443-f471-4970-85e3-419fb7f6e355",
        "TotalCnt": 1,
        "OperandList": [
            "组件",
            "节点",
            "集群"
        ],
        "SecurityLevelList": [
            "一般",
            "危险",
            "高危"
        ]
    }
}
```

