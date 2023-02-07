**Example 1: 查询指定数据库的备份数据表**



Input: 

```
tccli cdb DescribeBackupTables --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --DatabaseName mysql \
    --StartTime 2017-07-12 10:29:20
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": "28",
        "Items": [
            {
                "TableName": "general_log"
            },
            {
                "TableName": "slow_log"
            },
            {
                "TableName": "columns_priv"
            },
            {
                "TableName": "db"
            },
            {
                "TableName": "event"
            },
            {
                "TableName": "func"
            },
            {
                "TableName": "help_category"
            },
            {
                "TableName": "help_keyword"
            },
            {
                "TableName": "help_relation"
            },
            {
                "TableName": "help_topic"
            },
            {
                "TableName": "innodb_index_stats"
            },
            {
                "TableName": "innodb_table_stats"
            },
            {
                "TableName": "ndb_binlog_index"
            },
            {
                "TableName": "plugin"
            },
            {
                "TableName": "proc"
            },
            {
                "TableName": "procs_priv"
            },
            {
                "TableName": "proxies_priv"
            },
            {
                "TableName": "servers"
            },
            {
                "TableName": "slave_master_info"
            },
            {
                "TableName": "slave_relay_log_info"
            },
            {
                "TableName": "slave_worker_info"
            },
            {
                "TableName": "tables_priv"
            },
            {
                "TableName": "time_zone"
            },
            {
                "TableName": "time_zone_leap_second"
            },
            {
                "TableName": "time_zone_name"
            },
            {
                "TableName": "time_zone_transition"
            },
            {
                "TableName": "time_zone_transition_type"
            },
            {
                "TableName": "user"
            }
        ]
    }
}
```

