**Example 1: 获取产品级任务列表示例**



Input: 

```
tccli iotcloud DescribeProductTasks --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "TaskInfos": [
            {
                "BatchCount": 2,
                "ResultType": "cosfile",
                "Id": 1,
                "BatchOffset": 2,
                "CompleteTime": 1585626105,
                "Result": "https://iothub-tasktest-****",
                "CreateTime": 1585626105,
                "UpdateTime": 1585826608,
                "ParametersType": "cosfile",
                "Type": 0,
                "State": 5,
                "Parameters": "{\"filename\":\"input1.csv\",\"productType\":0,\"productEncryption\":1}"
            },
            {
                "CompleteTime": 1586228643,
                "ParametersType": "random",
                "BatchCount": 1,
                "Id": 1000000,
                "Parameters": "{\"batchNum\":1,\"productEncryption\":21,\"productType\":0}",
                "BatchOffset": 1,
                "CreateTime": 1586228643,
                "Type": 0,
                "ResultType": "cosfile",
                "UpdateTime": 1586228649,
                "Result": "https://iothub-tasktest-*****",
                "State": 5
            },
            {
                "Result": "https://iothub-tasktest-*****",
                "ParametersType": "random",
                "BatchCount": 1,
                "BatchOffset": 1,
                "State": 5,
                "UpdateTime": 1586228669,
                "Type": 0,
                "CompleteTime": 1586228663,
                "Parameters": "{\"batchNum\":1,\"productEncryption\":21,\"productType\":0}",
                "CreateTime": 1586228663,
                "ResultType": "cosfile",
                "Id": 1000001
            }
        ],
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

