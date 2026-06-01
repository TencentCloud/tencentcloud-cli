**Example 1: profile信息查询**



Input: 

```
tccli tchousex DescribeInstanceProfile --cli-unfold-argument  \
    --InstanceId instance-7wxclv93 \
    --QueryId 9744fcb875d5cf7c:73e1f09a00000000
```

Output: 
```
{
    "Response": {
        "RequestId": "test",
        "ErrorMsg": "",
        "ProfileStr": "Query (id=9744fcb875d5cf7c:73e1f09a00000000):\n   - InactiveTotalTime: 0.000ns\n   - TotalTime: 0.000ns\n  Summary:\n    Session ID: 10471c7475befb05:1c66610b4adb5698\n    Session Type: MYSQLSERVER\n    Start Time: 2025-05-21 19:29:07.779065000\n    End Time: 2025-05-21 19:29:07.786957000\n    Query Type: DDL\n    Query State: FINISHED\n    Impala Query State: FINISHED\n    Query Status: OK\n    TCHouseX Version: origin/1.8.0_DEV RELEASE (build 090c91a44792551a08633ecdc8b2ba64055402b3)\n    User: admin\n    Connected User: admin\n    Delegated User: \n    Network Address: 11.163.3.77:56628\n    Default Db: default\n    Sql Statement: SHOW TABLE STATS `inside_db`.`tbl_col13_parquet2`\n    Coordinator: 9.0.19.49:27000\n    Query Options (set by configuration): MT_DOP=4,TIMEZONE=Asia/Shanghai,OPTIMIZE_USING_METACACHE=0,OPTIMIZE_USING_RESULTCACHE=0,RESULT_CACHE_RECORD_NUM_LIMIT=10240,PREREAD_DATA_CACHE=0\n    Query Options (set by configuration and planner): MT_DOP=4,TIMEZONE=Asia/Shanghai,OPTIMIZE_USING_METACACHE=0,OPTIMIZE_USING_RESULTCACHE=0,RESULT_CACHE_RECORD_NUM_LIMIT=10240,PREREAD_DATA_CACHE=0\n    DDL Type: SHOW_STATS\n    DDL execution mode: synchronous\n    Query Compilation: 7.067ms\n       - Metadata of all 1 tables cached: 266.401us (266.401us)\n       - Analysis finished: 349.558us (83.157us)\n       - Authorization finished (ranger): 6.965ms (6.616ms)\n       - Planning finished: 7.067ms (101.960us)\n    Query Timeline: 8.000ms\n       - Query submitted: 0.000ns (0.000ns)\n       - Planning finished: 8.000ms (8.000ms)\n       - Rows available: 8.000ms (0.000ns)\n       - Unregister query: 8.000ms (0.000ns)\n     - InactiveTotalTime: 0.000ns\n     - TotalTime: 0.000ns\n    Frontend:\n       - InactiveTotalTime: 0.000ns\n       - TotalTime: 0.000ns\n  ImpalaServer:\n     - ClientFetchWaitTimer: 0.000ns\n     - InactiveTotalTime: 0.000ns\n     - NumRowsFetched: 0 (0)\n     - NumRowsFetchedFromCache: 0 (0)\n     - RowMaterializationRate: 0\n     - RowMaterializationTimer: 0.000ns\n     - TotalTime: 0.000ns\n"
    }
}
```

