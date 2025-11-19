**Example 1: 获取指定小版本下的Session配置**

本接口用于获取指定小版本下的Session配置。

Input: 

```
tccli dlc DescribeDataEngineSessionParameters --cli-unfold-argument  \
    --DataEngineId DataEngine-1
```

Output: 
```
{
    "Response": {
        "DataEngineParameters": [
            {
                "ParameterType": 1,
                "UpdateTime": "2020-01-01 01:01:01",
                "ValueLengthLimit": "100",
                "ValueType": "string",
                "IsPublic": 1,
                "ParameterId": "d3018ad4-9a7e-4f64-a3f4-f38507c69742",
                "KeyDescription": "默认分区数。",
                "KeyName": "spark.sql.shuffle.partitions",
                "ChildImageVersionId": "d30dfgsf4-9a7e-4f64-a3f4-f38507c69742",
                "ValueRegexpLimit": "[0-9]+$",
                "InsertTime": "2020-01-01 01:01:01",
                "Operator": "admin",
                "EngineType": "SparkSQL",
                "ValueDefault": "200",
                "SubmitMethod": "User"
            }
        ],
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

