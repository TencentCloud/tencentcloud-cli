**Example 1: 查看产品任务详情示例**



Input: 

```
tccli iotcloud DescribeProductTask --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "TaskInfo": {
            "ResultType": "cosfile",
            "Type": 0,
            "Parameters": "{\"filename\":\"input.csv\",\"productType\":0,\"productEncryption\":1}",
            "Result": "https://iothub-tasktest-****",
            "BatchOffset": 2,
            "UpdateTime": 1585826608,
            "State": 5,
            "ParametersType": "cosfile",
            "CreateTime": 1585626105,
            "Id": 1,
            "CompleteTime": 1585626105,
            "BatchCount": 2
        },
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

