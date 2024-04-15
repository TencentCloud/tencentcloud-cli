**Example 1: 请求demo**



Input: 

```
tccli wedata SubmitSqlTask --cli-unfold-argument  \
    --ProjectId 148541391437111111111 \
    --DatasourceType HIVE \
    --DatasourceId 1111 \
    --GroupId 20240409111111111 \
    --ResourceQueue default \
    --ComputeResource  \
    --DatabaseName  \
    --ConfParams {"RunConfParams":"","AdhocFileName":"sqldemo.sql","ResourceConfParams":{}} \
    --DatabaseType HIVE \
    --ScriptId c6bff4c1-3ff1-4765-82b6-1111111 \
    --ScriptContent LS1T \
    --ScriptEncryption True \
    --RunParams 
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "EndTime": null,
                "Id": 43248,
                "RecordId": 30388,
                "ScriptContent": "select 1",
                "StartTime": null,
                "Status": "WAITING"
            }
        ],
        "Record": {
            "CreateTime": "2024-04-15T15:36:34+08:00",
            "Id": 30388,
            "InstanceId": "6202404151536358025_2024-04-15T15:36:35+08:00",
            "ScriptContent": "\n\n\n\n\nselect 1\n",
            "Status": "WAITING"
        },
        "RequestId": "65e7142b-7d21-4df8-af43-b5705a6f8923"
    }
}
```

