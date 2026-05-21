**Example 1: 示例1**



Input: 

```
tccli wedata ListTaskRunningLog --cli-unfold-argument  \
    --WorkspaceId 17697667906247629 \
    --TaskId ta-e1ca6861 \
    --JobId cql-2c9a0ijf \
    --EndTime 1779187800000 \
    --StartTime 1779184200000 \
    --Container cql-2c9a0ijf-258045-taskmanager-1-1 \
    --Limit 3000 \
    --OrderType asc \
    --RunningOrderId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ListOver": false,
            "LogContentList": [
                {
                    "ContainerName": "cql-2c9a0ijf-258045-taskmanager-1-1",
                    "Log": "2026-05-19 17:50:19.301 [+08:00][RowDataExtractor -> SchemaClient -> Writer (1/1)#1] INFO  org.apache.inlong.sort.iceberg.common.AbstractMultipleIcebergTableSink - beforeSnapshotState get registeredOperatorStates.size:1 getIndexOfThisSubtask:0",
                    "PkgId": "207617D375D7235B-4",
                    "PkgLogId": "1376256",
                    "Time": "1779184219000"
                }
            ],
            "NextOffset": "Y29udGV4dC1kYTE1N2FiZi05YWNmLTQ4Y2YtYjMwZS1kYTk0OTQxYWIyNTcxNzc5MTk4NDkxMDg2"
        },
        "RequestId": "17bdbad8-aecb-4e90-a6a9-11eb50ff3286"
    }
}
```

