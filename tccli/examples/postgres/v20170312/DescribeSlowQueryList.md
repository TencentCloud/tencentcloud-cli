**Example 1: 慢SQL列表查询示例**



Input: 

```
tccli postgres DescribeSlowQueryList --cli-unfold-argument  \
    --StartTime 2021-07-22 10:00:07 \
    --EndTime 2021-07-27 20:15:07 \
    --Limit 10 \
    --Offset 0 \
    --DBInstanceId postgres-nbvqjlhf
```

Output: 
```
{
    "Response": {
        "DurationAnalysis": [
            {
                "Count": 0,
                "TimeSegment": "10-20s"
            },
            {
                "Count": 0,
                "TimeSegment": "40-50s"
            },
            {
                "Count": 0,
                "TimeSegment": "50s-"
            },
            {
                "Count": 0,
                "TimeSegment": "5-6s"
            },
            {
                "Count": 0,
                "TimeSegment": "6-7s"
            },
            {
                "Count": 0,
                "TimeSegment": "2-3s"
            },
            {
                "Count": 0,
                "TimeSegment": "20-30s"
            },
            {
                "Count": 0,
                "TimeSegment": "3-4s"
            },
            {
                "Count": 0,
                "TimeSegment": "4-5s"
            },
            {
                "Count": 0,
                "TimeSegment": "7-8s"
            },
            {
                "Count": 0,
                "TimeSegment": "8-9s"
            },
            {
                "Count": 0,
                "TimeSegment": "9-10s"
            },
            {
                "Count": 0,
                "TimeSegment": "30-40s"
            },
            {
                "Count": 6,
                "TimeSegment": "1-2s"
            }
        ],
        "RawSlowQueryList": [
            {
                "ClientAddr": "[local]",
                "DatabaseName": "postgres",
                "Duration": 101.013,
                "RawQuery": "select 1 from information_schema.tables where table_schema = 'pg_catalog' and table_name = 'pg_file_settings'",
                "SessionStartTime": "2021-07-27 03:12:01 CST",
                "UserName": "postgres"
            },
            {
                "ClientAddr": "::1:34301",
                "DatabaseName": "postgres",
                "Duration": 155.283,
                "RawQuery": "select count(*)::text as value from pg_stat_activity where now()-backend_start < '5  second';",
                "SessionStartTime": "2021-07-25 02:25:09 CST",
                "UserName": "postgres"
            },
            {
                "ClientAddr": "::1:34295",
                "DatabaseName": "postgres",
                "Duration": 168.119,
                "RawQuery": "select count(*)::text as value from pg_stat_activity where state='active';",
                "SessionStartTime": "2021-07-25 02:25:09 CST",
                "UserName": "postgres"
            },
            {
                "ClientAddr": "::1:34296",
                "DatabaseName": "postgres",
                "Duration": 168.757,
                "RawQuery": "select count(*)::text as value from pg_stat_activity where wait_event_type is not null",
                "SessionStartTime": "2021-07-25 02:25:09 CST",
                "UserName": "postgres"
            },
            {
                "ClientAddr": "::1:34298",
                "DatabaseName": "postgres",
                "Duration": 165.119,
                "RawQuery": "select application_name,COALESCE(pg_catalog.pg_wal_lsn_diff(sent_lsn, replay_lsn),0) from pg_stat_replication;",
                "SessionStartTime": "2021-07-25 02:25:09 CST",
                "UserName": "postgres"
            },
            {
                "ClientAddr": "::1:34297",
                "DatabaseName": "postgres",
                "Duration": 104.795,
                "RawQuery": "select count(*)::text as value from pg_stat_activity where state='idle';",
                "SessionStartTime": "2021-07-25 02:25:09 CST",
                "UserName": "postgres"
            }
        ],
        "RequestId": "221334ddcf",
        "TotalCount": 6
    }
}
```

