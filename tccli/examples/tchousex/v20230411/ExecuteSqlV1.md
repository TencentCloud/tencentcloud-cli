**Example 1: ExecutionSqlV1**

SQL工作区SQL执行接口

Input: 

```
tccli tchousex ExecuteSqlV1 --cli-unfold-argument  \
    --SqlToken eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6IjcyZGUwNGE1LWUzNDctNDRkNC1iZGY5LTRjYTEwNDRiZTBhOSIsImF1dGhvcml6ZWQiOnRydWUsImluc3RhbmNlX2lkIjoiaW5zdGFuY2UtMTMzZWh4N2MiLCJ1c2VyX25hbWUiOiJyb290In0.-AwzdJQuYvC_QIkdU1w9k_87oczeFsAQqJO9q8XeJVI \
    --InstanceId instance-test \
    --Cluster vw-7zxbmt5h \
    --Database default \
    --Sql aW5zZXJ0IGludG8gdGVzdF9kYXRhYmFzZS50ZXN0X3RhYmxlKGksIGQsIHMsIGR0LCB0cywgZHMpIHZhbHVlcygxLCAxLjAsICd0ZXN0JywgJzIwMjQtNC0yNCcsICcyMDIyLTEyLTMxIDIzOjU5OjU5JywgJzIwMjQwNDI0Jyk7 \
    --SessionId 00fe9e18-b06f-4c68-b9b9-62749f7d2729 \
    --AIGenerated 0
```

Output: 
```
{
    "Response": {
        "InstanceId": "",
        "ErrorMsg": "runtime error: index out of range [0] with length 0",
        "ErrMsg": "",
        "ReturnData": "{\"Sql\":\"insert into test_database.test_table(i, d, s, dt, ts, ds) values(1, 1.0, 'test', '2024-4-24', '2022-12-31 23:59:59', '20240424');\",\"IsQuery\":false,\"Columns\":null,\"ColumnType\":null,\"Values\":null,\"Offset\":0,\"Limit\":10000000,\"Total\":0,\"StartTime\":\"2024-12-19 17:07:51\",\"ExecuteTime\":24,\"ExecutionMsg\":\"err runtime error: index out of range [0] with length 0\",\"Success\":false,\"Host\":\"\",\"ProfileRes\":{\"QueryCompilation\":\"\",\"CompletedAdmission\":\"\",\"LastRowFetched\":\"\",\"TotalBytesRead\":\"\"},\"TaskId\":\"tchousex-xpfxcg\",\"TotalResultNum\":0,\"ResultCosId\":\"\",\"DownloadUrl\":\"\",\"SqlType\":0,\"SparkSqlTaskId\":\"\",\"Source\":0,\"UUID\":\"\",\"Status\":0,\"Creator\":\"100039840835\",\"SessionId\":\"00fe9e18-b06f-4c68-b9b9-62749f7d2729\",\"Database\":\"default\"}",
        "RequestId": "e465495a-5bbb-4984-85e5-0bf9739f8e00"
    }
}
```

