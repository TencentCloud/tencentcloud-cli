**Example 1: 查询任务指标信息**



Input: 

```
tccli wedata GetIntegrationTaskMetrics --cli-unfold-argument  \
    --WorkspaceId test_workspace_01 \
    --TaskId 4313be0b-742d-4dd9-afa8-08281047188e \
    --JobId 6820251229230121089
```

Output: 
```
{
    "Response": {
        "Data": {
            "ByteSpeed": 3,
            "ExecJobStatus": "",
            "JobId": "6820251229230121089",
            "Percentage": 1,
            "ReadSucceedBytes": "38",
            "ReadSucceedRecords": "5",
            "RecordSpeed": "0",
            "RunEndTime": "1760011946052",
            "RunStartTime": "1760011936031",
            "RunUserName": "zhangsan",
            "RunUserUin": "600000561778",
            "SinkDatasource": "v_vdzhimi.example_table_3",
            "SinkNodeName": "OUTPUT",
            "SourceDatasource": "v_vdzhimi.example_table",
            "SourceNodeName": "INPUT",
            "TaskId": "4313be0b-742d-4dd9-afa8-08281047188e",
            "TaskName": "testName",
            "TotalErrorBytes": "0",
            "TotalErrorRecords": "0",
            "TotalReadBytes": "38",
            "TotalReadRecords": "5",
            "WaitReaderTime": "0",
            "WaitWriterTime": "67747",
            "WorkspaceId": "test_workspace_01",
            "WriteReceivedBytes": "38",
            "WriteReceivedRecords": "5",
            "WriteSucceedBytes": "38",
            "WriteSucceedRecords": "5"
        },
        "RequestId": "391a0938-049e-43bd-b48e-0caf5b613d5f"
    }
}
```

