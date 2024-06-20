**Example 1: 获取SparkSQL批任务消耗**

获取SparkSQL批任务消耗

Input: 

```
tccli dlc DescribeSparkSessionBatchSQLCost --cli-unfold-argument  \
    --BatchIds d3018ad4-9a7e-4f64-a3f4-fsjr37c69742
```

Output: 
```
{
    "Response": {
        "CostInfo": [
            {
                "BatchId": "892499-8b41-1f5a213689f0",
                "DataEngineName": "engine_jar",
                "DataEngineId": "DataEngine-xxxx",
                "Cost": 0.7466666666666667,
                "TimeCost": 193,
                "Operator": "1000fsdf0"
            }
        ],
        "RequestId": "2ae4707a-9f72-sdfsd-sdf-cac3c2bc"
    }
}
```

