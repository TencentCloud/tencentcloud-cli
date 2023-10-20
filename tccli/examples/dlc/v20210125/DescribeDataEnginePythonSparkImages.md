**Example 1: 获取PYSPARK镜像列表**

本接口用于获取PYSPARK镜像列表。

Input: 

```
tccli dlc DescribeDataEnginePythonSparkImages --cli-unfold-argument  \
    --ChildImageVersionId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "PythonSparkImages": [
            {
                "UpdateTime": "2020-01-01:00:00:00",
                "Description": "测试",
                "ChildImageVersionId": "d3ksjed4-9a7e-4f64-a3f4-f38507c69742",
                "SparkImageId": "d3018ad4-9a7e-4f64-a3f4-f38507c69742",
                "SparkImageVersion": "测试镜像",
                "CreateTime": "2020-01-01:00:00:00"
            }
        ]
    }
}
```

