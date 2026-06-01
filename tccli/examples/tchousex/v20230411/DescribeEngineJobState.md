**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeEngineJobState --cli-unfold-argument  \
    --InstanceId warehouse-qiwlg758 \
    --EngineJobId batch-task-dmrqzc
```

Output: 
```
{
    "Response": {
        "CostTime": 162000,
        "CreateTime": "2023-12-05 15:50:19",
        "ErrorMsg": "",
        "Percentage": 0,
        "RequestId": "62aaa815-5697-4e30-8323-80e7dd7210cc",
        "State": 2
    }
}
```

