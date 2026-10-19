**Example 1: 查询阻塞日志详情**

查询阻塞日志详情

Input: 

```
tccli dbbrain DescribeBlockingLogs --cli-unfold-argument  \
    --InstanceId mssql-15rso1sb \
    --Product sqlserver \
    --StartTime 2026-10-15 21:00:00 \
    --EndTime 2026-10-15 21:15:00 \
    --WithXml True
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BlockedClientApp": "SQLAgent - TSQL JobStep (Job 0x18EF8CB8CF2AFD4FB112247D30FE8605 : Step 1)",
                "BlockedHostName": "TEN-4DUQ5CVE6R",
                "BlockedInputBuffer": "EXEC DBO.JOB_MONITOR_FILTER",
                "BlockedIsolationLevel": "read committed (2)",
                "BlockedLastTranStarted": "2026-10-15T13:12:26.417",
                "BlockedLockMode": "Sch-S",
                "BlockedLoginName": "app_user",
                "BlockedProcessXml": "<blocked-process-report monitorLoop=\"2123355\">\r\n <blocked-process>\r\n  <process id=\"process08cce44605\" taskpriority=\"0\" logused=\"0\" waitresource=\"KEY: 7:115467663 (a0982edbe93f50f5) \" waittime=\"42607\" ownerId=\"749987700\" transactionname=\"INSERT\" lasttranstarted=\"2026-10-15T13:12:26.417\" XDES=\"0x0xa570b5da6773d\" lockMode=\"Sch-S\" schedulerid=\"8\" kpid=\"78426\" status=\"suspended\" spid=\"116\" sbid=\"0\" ecid=\"0\" priority=\"0\" trancount=\"2\" lastbatchstarted=\"2026-10-15T13:12:26.850\" lastbatchcompleted=\"2026-10-15T13:12:26.850\" lastattention=\"1900-01-01T00:00:00.327\" clientapp=\"SQLAgent - TSQL JobStep (Job 0x18EF8CB8CF2AFD4FB112247D30FE8605 : Step 1)\" hostname=\"TEN-4DUQ5CVE6R\" hostpid=\"50025\" loginname=\"app_user\" isolationlevel=\"read committed (2)\" xactid=\"749987700\" currentdb=\"7\" currentdbname=\"reportdb\" lockTimeout=\"4294967295\" clientoption1=\"673185824\" clientoption2=\"128056\">\r\n   <executionStack>\r\n    <frame line=\"11\" stmtstart=\"57916\" stmtend=\"27743\" sqlhandle=\"0x030005002b567886d367cec25c516e540c4f7a1ee4f05a8f87252afc8e4abe27dc9cc72a43cf68c30000000000000000000000000000000000000000\"/>\r\n    <frame line=\"1\" stmtend=\"52\" sqlhandle=\"0x030005007a75416b29235ec6317951ec353e9af1a86d81d7941b638d7f4e6a883bcfd5798a26a8870000000000000000000000000000000000000000\"/>\r\n   </executionStack>\r\n   <inputbuf>\r\nEXEC DBO.JOB_MONITOR_FILTER   </inputbuf>\r\n  </process>\r\n </blocked-process>\r\n <blocking-process>\r\n  <process status=\"suspended\" spid=\"120\" sbid=\"0\" ecid=\"0\" priority=\"0\" trancount=\"2\" lastbatchstarted=\"2026-10-15T13:12:26.820\" lastbatchcompleted=\"2026-10-15T13:12:26.820\" lastattention=\"1900-01-01T00:00:00.664\" clientapp=\"SQLAgent - TSQL JobStep (Job 0x8FA6C0ECC85510429881508623587978 : Step 1)\" hostname=\"TEN-4DUQ5CVE6R\" hostpid=\"50025\" loginname=\"sa\" isolationlevel=\"read committed (2)\" xactid=\"749941246\" currentdb=\"7\" currentdbname=\"reportdb\" lockTimeout=\"4294967295\" clientoption1=\"673185824\" clientoption2=\"128056\">\r\n   <executionStack>\r\n    <frame line=\"278\" stmtstart=\"19639\" stmtend=\"20836\" sqlhandle=\"0x0300050010cf5e13b947f01843d20fc9f62fe896ba621d42291aa485b93d5188c21b7d4e86817a7b0000000000000000000000000000000000000000\"/>\r\n    <frame line=\"5\" stmtstart=\"94\" stmtend=\"170\" sqlhandle=\"0x0300050070304dc2f0940d07fe829a9ce01dd7ee9159e405acb43e0ad8984b85b61c56e716e64ac00000000000000000000000000000000000000000\"/>\r\n   </executionStack>\r\n   <inputbuf>\r\nSELECT COUNT(*) FROM DBO.LARGE_TABLE WITH (TABLOCKX)   </inputbuf>\r\n  </process>\r\n </blocking-process>\r\n</blocked-process-report>\r\n",
                "BlockedSessionId": 116,
                "BlockedSqlMd5": "05c5e788a3fe2ace9f63efd9bee972c8",
                "BlockedSqlTemplate": "EXEC DBO.JOB_MONITOR_FILTER",
                "BlockedStatus": "suspended",
                "BlockedTranCount": 2,
                "BlockedTransactionId": 749987700,
                "BlockedTransactionName": "INSERT",
                "BlockedWaitResource": "KEY: 7:115467663 (a0982edbe93f50f5) ",
                "BlockedWaitTimeMs": 42607,
                "BlockingClientApp": "SQLAgent - TSQL JobStep (Job 0x8FA6C0ECC85510429881508623587978 : Step 1)",
                "BlockingHostName": "TEN-4DUQ5CVE6R",
                "BlockingInputBuffer": "SELECT COUNT(*) FROM DBO.LARGE_TABLE WITH (TABLOCKX)",
                "BlockingIsolationLevel": "read committed (2)",
                "BlockingLastTranStarted": "",
                "BlockingLockMode": "",
                "BlockingLoginName": "sa",
                "BlockingSessionId": 120,
                "BlockingSqlMd5": "2a1826132ed238dfb711c241f09b42a9",
                "BlockingSqlTemplate": "SELECT COUNT(*) FROM DBO.LARGE_TABLE WITH (TABLOCKX)",
                "BlockingStatus": "suspended",
                "BlockingTranCount": 2,
                "BlockingTransactionName": "",
                "BlockingWaitTimeMs": 0,
                "DatabaseName": "reportdb",
                "DurationMs": 42607,
                "MonitorLoop": "2123355",
                "ReportTime": "2026-10-15 21:12:26",
                "RootCause": "C1_LONG_QUERY",
                "RootCauseDesc": "长事务查询持锁"
            }
        ],
        "TotalCount": 63,
        "RequestId": "88eb3bd5-21aa-402b-99e3-1fa51fdc3640"
    }
}
```

