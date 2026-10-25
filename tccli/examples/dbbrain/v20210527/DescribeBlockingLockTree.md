**Example 1: 查询某时间点的阻塞会话树**

查询某时间点的阻塞会话树

Input: 

```
tccli dbbrain DescribeBlockingLockTree --cli-unfold-argument  \
    --InstanceId mssql-15rso1sb \
    --MonitorLoop 1000782 \
    --Product sqlserver
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BlockingStatus": "suspended",
                "BlockingClientApp": "python-pymssql",
                "DurationMs": 8342,
                "EndTime": "2026-10-21 21:05:33",
                "BlockingSqlMd5": "d4b1ea0c9f6e17bbc45ec3495486aa88",
                "BlockingSessionId": 582,
                "DatabaseName": "Monitor",
                "RootCauseDesc": "长查询正常运行阻塞，考虑优化 SQL/索引",
                "StartTime": "2026-10-21 21:05:33",
                "BlockingIsolationLevel": "read committed (2)",
                "BlockingTransactionId": 715360384,
                "ChainDepth": 9,
                "BlockingTranCount": 2,
                "BlockingWaitTimeMs": 0,
                "BlockingSqlTemplate": "EXEC DBO.SP_LONG_LOCK_HOLDER @HOLD_MINUTES = ?",
                "MonitorLoop": "1000782",
                "Details": [
                    {
                        "BlockedHostName": "TEN-4DUQ5CVE6R",
                        "BlockedStatus": "suspended",
                        "BlockedTransactionId": 715360384,
                        "BlockedWaitTimeMs": 8342,
                        "BlockedInputBuffer": "UPDATE DBO.ORDER_TABLE SET STATUS = 'DONE' WHERE ID = 1",
                        "BlockedTranCount": 3,
                        "BlockedLoginName": "report_svc",
                        "BlockedClientApp": "python-pymssql",
                        "BlockedSqlMd5": "7d944d41c2e6dabe7a888207c073288d",
                        "BlockedLockMode": "X",
                        "BlockedLastTranStarted": "2026-10-21 19:20:05",
                        "BlockedSqlTemplate": "UPDATE DBO.ORDER_TABLE SET STATUS = ? WHERE ID = ?",
                        "ReportTime": "2026-10-21 21:05:33",
                        "BlockedWaitResource": "KEY: 14:1732724499 (70f59de93dea) ",
                        "BlockedIsolationLevel": "serializable (4)",
                        "RootCause": "C1_LONG_QUERY",
                        "Children": [
                            {
                                "BlockedHostName": "TEN-4DUQ5CVE6R",
                                "BlockedStatus": "suspended",
                                "BlockedTransactionId": 824994255,
                                "BlockedWaitTimeMs": 8274,
                                "BlockedInputBuffer": "UPDATE DBO.T_KEY SET V = V + 1 WHERE ID = 1",
                                "BlockedTranCount": 3,
                                "BlockedLoginName": "test_g",
                                "BlockedClientApp": ".Net SqlClient Data Provider",
                                "BlockedSqlMd5": "800207e64961b44b4abf0152e1260cf6",
                                "BlockedLockMode": "X",
                                "BlockedLastTranStarted": "2026-10-21 19:20:09",
                                "BlockedSqlTemplate": "UPDATE DBO.T_KEY SET V = V + ? WHERE ID = ?",
                                "ReportTime": "2026-10-21 21:05:33",
                                "BlockedWaitResource": "KEY: 14:1732724499 (70f59de93dea) ",
                                "BlockedIsolationLevel": "repeatable read (3)",
                                "RootCause": "C1_LONG_QUERY",
                                "Children": [
                                    {
                                        "BlockedHostName": "TEN-4DUQ5CVE6R",
                                        "BlockedStatus": "suspended",
                                        "BlockedTransactionId": 653057905,
                                        "BlockedWaitTimeMs": 8280,
                                        "BlockedInputBuffer": "UPDATE DBO.ORDER_TABLE SET AMOUNT = AMOUNT + 1 WHERE ID = 1",
                                        "BlockedTranCount": 3,
                                        "BlockedLoginName": "app_user",
                                        "BlockedClientApp": "jdbc-mssql",
                                        "BlockedSqlMd5": "85db6335df7303b20445750457f23fec",
                                        "BlockedLockMode": "X",
                                        "BlockedLastTranStarted": "2026-10-21 19:20:18",
                                        "BlockedSqlTemplate": "UPDATE DBO.ORDER_TABLE SET AMOUNT = AMOUNT + ? WHERE ID = ?",
                                        "ReportTime": "2026-10-21 21:05:33",
                                        "BlockedWaitResource": "KEY: 14:1732724499 (70f59de93dea) ",
                                        "BlockedIsolationLevel": "repeatable read (3)",
                                        "RootCause": "C1_LONG_QUERY",
                                        "Children": [
                                            {
                                                "BlockedHostName": "TEN-4DUQ5CVE6R",
                                                "BlockedStatus": "suspended",
                                                "BlockedTransactionId": 763820642,
                                                "BlockedWaitTimeMs": 8251,
                                                "BlockedInputBuffer": "UPDATE DBO.ORDER_TABLE SET AMOUNT = AMOUNT + 1 WHERE ID = 1",
                                                "BlockedTranCount": 3,
                                                "BlockedLoginName": "app_user",
                                                "BlockedClientApp": "jdbc-mssql",
                                                "BlockedSqlMd5": "85db6335df7303b20445750457f23fec",
                                                "BlockedLockMode": "X",
                                                "BlockedLastTranStarted": "2026-10-21 19:20:19",
                                                "BlockedSqlTemplate": "UPDATE DBO.ORDER_TABLE SET AMOUNT = AMOUNT + ? WHERE ID = ?",
                                                "ReportTime": "2026-10-21 21:05:33",
                                                "BlockedWaitResource": "KEY: 14:1732724499 (70f59de93dea) ",
                                                "BlockedIsolationLevel": "serializable (4)",
                                                "RootCause": "C1_LONG_QUERY",
                                                "Children": [
                                                    {
                                                        "BlockedHostName": "TEN-4DUQ5CVE6R",
                                                        "BlockedStatus": "suspended",
                                                        "BlockedTransactionId": 551470879,
                                                        "BlockedWaitTimeMs": 8220,
                                                        "BlockedInputBuffer": "UPDATE DBO.ORDER_TABLE SET AMOUNT = AMOUNT + 1 WHERE ID = 1",
                                                        "BlockedTranCount": 3,
                                                        "BlockedLoginName": "test_g",
                                                        "BlockedClientApp": "python-pymssql",
                                                        "BlockedSqlMd5": "85db6335df7303b20445750457f23fec",
                                                        "BlockedLockMode": "X",
                                                        "BlockedLastTranStarted": "2026-10-21 19:20:23",
                                                        "BlockedSqlTemplate": "UPDATE DBO.ORDER_TABLE SET AMOUNT = AMOUNT + ? WHERE ID = ?",
                                                        "ReportTime": "2026-10-21 21:05:33",
                                                        "BlockedWaitResource": "KEY: 14:1732724499 (70f59de93dea) ",
                                                        "BlockedIsolationLevel": "read committed (2)",
                                                        "RootCause": "C1_LONG_QUERY",
                                                        "Children": [
                                                            {
                                                                "BlockedHostName": "TEN-4DUQ5CVE6R",
                                                                "BlockedStatus": "suspended",
                                                                "BlockedTransactionId": 594766386,
                                                                "BlockedWaitTimeMs": 7906,
                                                                "BlockedInputBuffer": "UPDATE DBO.T_KEY SET V = V + 1 WHERE ID = 1",
                                                                "BlockedTranCount": 3,
                                                                "BlockedLoginName": "test_g",
                                                                "BlockedClientApp": "python-pymssql",
                                                                "BlockedSqlMd5": "800207e64961b44b4abf0152e1260cf6",
                                                                "BlockedLockMode": "X",
                                                                "BlockedLastTranStarted": "2026-10-21 19:20:21",
                                                                "BlockedSqlTemplate": "UPDATE DBO.T_KEY SET V = V + ? WHERE ID = ?",
                                                                "ReportTime": "2026-10-21 21:05:33",
                                                                "BlockedWaitResource": "KEY: 14:1732724499 (70f59de93dea) ",
                                                                "BlockedIsolationLevel": "repeatable read (3)",
                                                                "RootCause": "C1_LONG_QUERY",
                                                                "Children": [
                                                                    {
                                                                        "BlockedHostName": "TEN-4DUQ5CVE6R",
                                                                        "BlockedStatus": "suspended",
                                                                        "BlockedTransactionId": 778620777,
                                                                        "BlockedWaitTimeMs": 8269,
                                                                        "BlockedInputBuffer": "UPDATE DBO.ORDER_TABLE SET STATUS = 'DONE' WHERE ID = 1",
                                                                        "BlockedTranCount": 3,
                                                                        "BlockedLoginName": "test_g",
                                                                        "BlockedClientApp": ".Net SqlClient Data Provider",
                                                                        "BlockedSqlMd5": "7d944d41c2e6dabe7a888207c073288d",
                                                                        "BlockedLockMode": "X",
                                                                        "BlockedLastTranStarted": "2026-10-21 19:20:38",
                                                                        "BlockedSqlTemplate": "UPDATE DBO.ORDER_TABLE SET STATUS = ? WHERE ID = ?",
                                                                        "ReportTime": "2026-10-21 21:05:33",
                                                                        "BlockedWaitResource": "KEY: 14:1732724499 (70f59de93dea) ",
                                                                        "BlockedIsolationLevel": "read committed (2)",
                                                                        "RootCause": "C1_LONG_QUERY",
                                                                        "Children": [
                                                                            {
                                                                                "BlockedHostName": "TEN-4DUQ5CVE6R",
                                                                                "BlockedStatus": "suspended",
                                                                                "BlockedTransactionId": 537998933,
                                                                                "BlockedWaitTimeMs": 7815,
                                                                                "BlockedInputBuffer": "SELECT * FROM DBO.ORDER_TABLE WITH (UPDLOCK) WHERE ID = 1",
                                                                                "BlockedTranCount": 3,
                                                                                "BlockedLoginName": "test_g",
                                                                                "BlockedClientApp": "jdbc-mssql",
                                                                                "BlockedSqlMd5": "6d93759d80eb316de6bd0954917fee13",
                                                                                "BlockedLockMode": "X",
                                                                                "BlockedLastTranStarted": "2026-10-21 19:20:43",
                                                                                "BlockedSqlTemplate": "SELECT * FROM DBO.ORDER_TABLE WITH (UPDLOCK) WHERE ID = ?",
                                                                                "ReportTime": "2026-10-21 21:05:33",
                                                                                "BlockedWaitResource": "KEY: 14:1732724499 (70f59de93dea) ",
                                                                                "BlockedIsolationLevel": "repeatable read (3)",
                                                                                "RootCause": "C1_LONG_QUERY",
                                                                                "Children": [
                                                                                    {
                                                                                        "BlockedHostName": "TEN-4DUQ5CVE6R",
                                                                                        "BlockedStatus": "suspended",
                                                                                        "BlockedTransactionId": 649799463,
                                                                                        "BlockedWaitTimeMs": 8084,
                                                                                        "BlockedInputBuffer": "SELECT * FROM DBO.ORDER_TABLE WITH (UPDLOCK) WHERE ID = 1",
                                                                                        "BlockedTranCount": 3,
                                                                                        "BlockedLoginName": "app_user",
                                                                                        "BlockedClientApp": "python-pymssql",
                                                                                        "BlockedSqlMd5": "6d93759d80eb316de6bd0954917fee13",
                                                                                        "BlockedLockMode": "X",
                                                                                        "BlockedLastTranStarted": "2026-10-21 19:20:30",
                                                                                        "BlockedSqlTemplate": "SELECT * FROM DBO.ORDER_TABLE WITH (UPDLOCK) WHERE ID = ?",
                                                                                        "ReportTime": "2026-10-21 21:05:33",
                                                                                        "BlockedWaitResource": "KEY: 14:1732724499 (70f59de93dea) ",
                                                                                        "BlockedIsolationLevel": "serializable (4)",
                                                                                        "RootCause": "C1_LONG_QUERY",
                                                                                        "BlockedSessionId": 6373,
                                                                                        "BlockedTransactionName": "user_transaction"
                                                                                    }
                                                                                ],
                                                                                "BlockedSessionId": 54501,
                                                                                "BlockedTransactionName": "SELECT"
                                                                            }
                                                                        ],
                                                                        "BlockedSessionId": 43103,
                                                                        "BlockedTransactionName": "UPDATE"
                                                                    }
                                                                ],
                                                                "BlockedSessionId": 36729,
                                                                "BlockedTransactionName": "UPDATE"
                                                            }
                                                        ],
                                                        "BlockedSessionId": 24711,
                                                        "BlockedTransactionName": "DELETE"
                                                    }
                                                ],
                                                "BlockedSessionId": 16211,
                                                "BlockedTransactionName": "DELETE"
                                            }
                                        ],
                                        "BlockedSessionId": 13767,
                                        "BlockedTransactionName": "DELETE"
                                    }
                                ],
                                "BlockedSessionId": 31618,
                                "BlockedTransactionName": "SELECT"
                            }
                        ],
                        "BlockedSessionId": 56501,
                        "BlockedTransactionName": "DELETE"
                    }
                ],
                "RootCause": "C1_LONG_QUERY",
                "BlockingInputBuffer": "EXEC DBO.SP_LONG_LOCK_HOLDER @hold_minutes = 30",
                "BlockingHostName": "TEN-4DUQ5CVE6R",
                "BlockingLoginName": "report_svc",
                "ChainLength": 9
            }
        ],
        "RequestId": "a3228322-385e-4237-8101-08c74b0dfda2"
    }
}
```

