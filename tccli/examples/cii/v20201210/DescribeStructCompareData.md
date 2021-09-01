**Example 1: 结构化对比查询接口示例**



Input: 

```
tccli cii DescribeStructCompareData --cli-unfold-argument  \
    --TaskId 37778536980168704
```

Output: 
```
{
    "Response": {
        "RequestId": "9317f6e4-6636-41a0-bf24-89ad9e4877f2",
        "PolicyId": "100001",
        "TaskId": "37778536980168704",
        "CustomerId": "100001",
        "CustomerName": "张三",
        "ReviewTime": "2020-12-19 18:43:37",
        "MachineResult": "{...}",
        "ManualResult": "{...}",
        "NewItems": "",
        "ModifyItems": "",
        "Metrics": {
            "ShortStructAccuracy": "95",
            "ShortStructRecall": "11",
            "LongStructAccuracy": "93",
            "LongStructRecall": "14",
            "LongContentAccuracy": "94",
            "LongContentRecall": "14"
        }
    }
}
```

