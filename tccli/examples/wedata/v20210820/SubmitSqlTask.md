**Example 1: 请求demo**



Input: 

```
tccli wedata SubmitSqlTask --cli-unfold-argument  \
    --DatabaseType abc \
    --DatabaseName abc \
    --DatasourceId 0 \
    --GroupId abc \
    --EngineId abc \
    --ScriptId abc \
    --ScriptContent abc \
    --ProjectId abc \
    --ResourceQueue abc \
    --DatasourceType abc \
    --ComputeResource abc \
    --RunParams abc \
    --ConfParams abc \
    --ScriptEncryption True
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

