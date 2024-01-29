**Example 1: pyspark 提交示例**

开发空间提交 pyspark 任务

Input: 

```
tccli wedata SubmitPySparkTask --cli-unfold-argument  \
    --GroupId abc \
    --ScriptPath abc \
    --ScriptContent abc \
    --ProjectId abc \
    --PythonType abc \
    --RunParams abc \
    --ScriptId abc \
    --ResourceQueue abc \
    --ConfigParams abc
```

Output: 
```
{
    "Response": {
        "Record": {
            "Id": 1,
            "ScriptContent": "abc",
            "CreateTime": "2020-09-22T00:00:00+00:00",
            "Status": "abc",
            "InstanceId": "abc"
        },
        "Details": [
            {
                "Id": 1,
                "ScriptContent": "abc",
                "StartTime": "2020-09-22T00:00:00+00:00",
                "EndTime": "2020-09-22T00:00:00+00:00",
                "Status": "abc",
                "RecordId": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

