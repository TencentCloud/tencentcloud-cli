**Example 1: Getting current database parameters**



Input: 

```
tccli mariadb DescribeDBParameters --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3
```

Output: 
```
{
    "Response": {
        "InstanceId": "tdsql-ige1a5k3",
        "Params": [
            {
                "Default": "1",
                "SetValue": "",
                "Value": "1",
                "Param": "auto_increment_increment",
                "Constraint": {
                    "Range": {
                        "Max": "65535",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "1",
                "SetValue": "",
                "Value": "1",
                "Param": "auto_increment_offset",
                "Constraint": {
                    "Range": {
                        "Max": "65535",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "ON",
                "SetValue": "",
                "Value": "ON",
                "Param": "autocommit",
                "Constraint": {
                    "Enum": "ON,OFF",
                    "Type": "enum"
                }
            },
            {
                "Default": "ROW",
                "SetValue": "",
                "Value": "ROW",
                "Param": "binlog_format",
                "Constraint": {
                    "Enum": "ROW,STATEMENT,MIXED",
                    "Type": "enum"
                }
            },
            {
                "Default": "utf8",
                "SetValue": "",
                "Value": "utf8",
                "Param": "character_set_server",
                "Constraint": {
                    "Enum": "utf8,latin1,gbk,utf8mb4",
                    "Type": "enum"
                }
            },
            {
                "Default": "",
                "SetValue": "",
                "Value": "utf8_general_ci",
                "Param": "collation_server",
                "Constraint": {
                    "Enum": "latin1_general_cs,latin1_general_ci,latin1_bin,latin1_swedish_ci,gbk_chinese_ci,gbk_bin,utf8_general_ci,utf8_bin,utf8_unicode_ci,utf8mb4_general_ci,utf8mb4_bin,utf8mb4_unicode_ci",
                    "Type": "enum"
                }
            },
            {
                "Default": "10",
                "SetValue": "",
                "Value": "10",
                "Param": "connect_timeout",
                "Constraint": {
                    "Range": {
                        "Max": "3600",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "0",
                "SetValue": "",
                "Value": "0",
                "Param": "default_week_format",
                "Constraint": {
                    "Range": {
                        "Max": "7",
                        "Min": "0"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "ON",
                "SetValue": "",
                "Value": "ON",
                "Param": "delay_key_write",
                "Constraint": {
                    "Enum": "ON,OFF,ALL",
                    "Type": "enum"
                }
            },
            {
                "Default": "100",
                "SetValue": "",
                "Value": "100",
                "Param": "delayed_insert_limit",
                "Constraint": {
                    "Range": {
                        "Max": "4294967295",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "300",
                "SetValue": "",
                "Value": "300",
                "Param": "delayed_insert_timeout",
                "Constraint": {
                    "Range": {
                        "Max": "3600",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "1000",
                "SetValue": "",
                "Value": "1000",
                "Param": "delayed_queue_size",
                "Constraint": {
                    "Range": {
                        "Max": "4294967295",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "4",
                "SetValue": "",
                "Value": "4",
                "Param": "div_precision_increment",
                "Constraint": {
                    "Range": {
                        "Max": "30",
                        "Min": "0"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "OFF",
                "SetValue": "",
                "Value": "OFF",
                "Param": "event_scheduler",
                "Constraint": {
                    "Enum": "ON,OFF",
                    "Type": "enum"
                }
            },
            {
                "Default": "1024",
                "SetValue": "",
                "Value": "1024",
                "Param": "group_concat_max_len",
                "Constraint": {
                    "Range": {
                        "Max": "18446744073709547520",
                        "Min": "4"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "5000",
                "SetValue": "",
                "Value": "5000",
                "Param": "innodb_concurrency_tickets",
                "Constraint": {
                    "Range": {
                        "Max": "10000",
                        "Min": "100"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "OFF",
                "SetValue": "",
                "Value": "ON",
                "Param": "innodb_large_prefix",
                "Constraint": {
                    "Enum": "OFF,ON",
                    "Type": "enum"
                }
            },
            {
                "Default": "50",
                "SetValue": "",
                "Value": "20",
                "Param": "innodb_lock_wait_timeout",
                "Constraint": {
                    "Range": {
                        "Max": "1073741824",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "10",
                "SetValue": "",
                "Value": "70.000000",
                "Param": "innodb_max_dirty_pages_pct",
                "Constraint": {
                    "Range": {
                        "Max": "90",
                        "Min": "10"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "37",
                "SetValue": "",
                "Value": "37",
                "Param": "innodb_old_blocks_pct",
                "Constraint": {
                    "Range": {
                        "Max": "95",
                        "Min": "5"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "1000",
                "SetValue": "",
                "Value": "1000",
                "Param": "innodb_old_blocks_time",
                "Constraint": {
                    "Range": {
                        "Max": "1000",
                        "Min": "0"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "4096",
                "SetValue": "",
                "Value": "16384",
                "Param": "innodb_page_size",
                "Constraint": {
                    "Enum": "4096,8192,16384,32768,65536",
                    "Type": "enum"
                }
            },
            {
                "Default": "300",
                "SetValue": "",
                "Value": "1000",
                "Param": "innodb_purge_batch_size",
                "Constraint": {
                    "Range": {
                        "Max": "1024",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "56",
                "SetValue": "",
                "Value": "56",
                "Param": "innodb_read_ahead_threshold",
                "Constraint": {
                    "Range": {
                        "Max": "64",
                        "Min": "0"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "nulls_equal",
                "SetValue": "",
                "Value": "nulls_equal",
                "Param": "innodb_stats_method",
                "Constraint": {
                    "Enum": "nulls_equal,nulls_unequal,nulls_ignored",
                    "Type": "enum"
                }
            },
            {
                "Default": "OFF",
                "SetValue": "",
                "Value": "OFF",
                "Param": "innodb_stats_on_metadata",
                "Constraint": {
                    "Enum": "ON,OFF",
                    "Type": "enum"
                }
            },
            {
                "Default": "8",
                "SetValue": "",
                "Value": "8",
                "Param": "innodb_stats_sample_pages",
                "Constraint": {
                    "Range": {
                        "Max": "4294967296",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "OFF",
                "SetValue": "",
                "Value": "OFF",
                "Param": "innodb_strict_mode",
                "Constraint": {
                    "Enum": "ON,OFF",
                    "Type": "enum"
                }
            },
            {
                "Default": "ON",
                "SetValue": "",
                "Value": "ON",
                "Param": "innodb_table_locks",
                "Constraint": {
                    "Enum": "ON,OFF",
                    "Type": "enum"
                }
            },
            {
                "Default": "0",
                "SetValue": "",
                "Value": "64",
                "Param": "innodb_thread_concurrency",
                "Constraint": {
                    "Range": {
                        "Max": "128",
                        "Min": "0"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "10000",
                "SetValue": "",
                "Value": "0",
                "Param": "innodb_thread_sleep_delay",
                "Constraint": {
                    "Range": {
                        "Max": "3600000",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "28800",
                "SetValue": "",
                "Value": "28800",
                "Param": "interactive_timeout",
                "Constraint": {
                    "Range": {
                        "Max": "86400",
                        "Min": "10"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "262144",
                "SetValue": "",
                "Value": "2097152",
                "Param": "join_buffer_size",
                "Constraint": {
                    "Range": {
                        "Max": "18446744073709547520",
                        "Min": "128"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "300",
                "SetValue": "",
                "Value": "300",
                "Param": "key_cache_age_threshold",
                "Constraint": {
                    "Range": {
                        "Max": "4294967295",
                        "Min": "100"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "1024",
                "SetValue": "",
                "Value": "1024",
                "Param": "key_cache_block_size",
                "Constraint": {
                    "Range": {
                        "Max": "16384",
                        "Min": "512"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "100",
                "SetValue": "",
                "Value": "100",
                "Param": "key_cache_division_limit",
                "Constraint": {
                    "Range": {
                        "Max": "100",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "5",
                "SetValue": "",
                "Value": "5",
                "Param": "lock_wait_timeout",
                "Constraint": {
                    "Range": {
                        "Max": "31536000",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "OFF",
                "SetValue": "",
                "Value": "OFF",
                "Param": "log_queries_not_using_indexes",
                "Constraint": {
                    "Enum": "ON,OFF",
                    "Type": "enum"
                }
            },
            {
                "Default": "1.000000",
                "SetValue": "",
                "Value": "1.000000",
                "Param": "long_query_time",
                "Constraint": {
                    "Range": {
                        "Max": "10",
                        "Min": "0.05"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "OFF",
                "SetValue": "",
                "Value": "OFF",
                "Param": "low_priority_updates",
                "Constraint": {
                    "Enum": "OFF,ON",
                    "Type": "enum"
                }
            },
            {
                "Default": "1",
                "SetValue": "",
                "Value": "0",
                "Param": "lower_case_table_names",
                "Constraint": {
                    "Enum": "0,1",
                    "Type": "enum"
                }
            },
            {
                "Default": "134217728",
                "SetValue": "",
                "Value": "1073741824",
                "Param": "max_allowed_packet",
                "Constraint": {
                    "Range": {
                        "Max": "1073741824",
                        "Min": "16384"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "2000",
                "SetValue": "",
                "Value": "2000",
                "Param": "max_connect_errors",
                "Constraint": {
                    "Range": {
                        "Max": "4096",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "4096",
                "SetValue": "",
                "Value": "10000",
                "Param": "max_connections",
                "Constraint": {
                    "Range": {
                        "Max": "32768",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "16382",
                "SetValue": "",
                "Value": "200000",
                "Param": "max_prepared_stmt_count",
                "Constraint": {
                    "Range": {
                        "Max": "1048576",
                        "Min": "0"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "4194304",
                "SetValue": "",
                "Value": "4194304",
                "Param": "myisam_sort_buffer_size",
                "Constraint": {
                    "Range": {
                        "Max": "16777216",
                        "Min": "262144"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "16384",
                "SetValue": "",
                "Value": "16384",
                "Param": "net_buffer_length",
                "Constraint": {
                    "Enum": "4096,8192,16384,32768,65536,1048576",
                    "Type": "enum"
                }
            },
            {
                "Default": "30",
                "SetValue": "",
                "Value": "30",
                "Param": "net_read_timeout",
                "Constraint": {
                    "Range": {
                        "Max": "3153600",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "10",
                "SetValue": "",
                "Value": "10",
                "Param": "net_retry_count",
                "Constraint": {
                    "Range": {
                        "Max": "4294967295",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "60",
                "SetValue": "",
                "Value": "60",
                "Param": "net_write_timeout",
                "Constraint": {
                    "Range": {
                        "Max": "3153600",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,optimize_join_buffer_size=on",
                "SetValue": "",
                "Value": "batched_key_access=off,block_nested_loop=on,condition_fanout_filter=on,derived_merge=on,duplicateweedout=on,engine_condition_pushdown=on,firstmatch=on,index_condition_pushdown=on,index_merge=on,index_merge_intersection=on,index_merge_sort_union=on,index_merge_union=on,loosescan=on,materialization=on,mrr=on,mrr_cost_based=on,semijoin=on,subquery_materialization_cost_based=on,use_index_extensions=on",
                "Param": "optimizer_switch",
                "Constraint": {
                    "Type": "string"
                }
            },
            {
                "Default": "8192",
                "SetValue": "",
                "Value": "16384",
                "Param": "query_alloc_block_size",
                "Constraint": {
                    "Range": {
                        "Max": "16384",
                        "Min": "1024"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "1048576",
                "SetValue": "",
                "Value": "1048576",
                "Param": "query_cache_limit",
                "Constraint": {
                    "Range": {
                        "Max": "1048576",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "0",
                "SetValue": "",
                "Value": "0",
                "Param": "query_cache_size",
                "Constraint": {
                    "Range": {
                        "Max": "104857600",
                        "Min": "0"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "OFF",
                "SetValue": "",
                "Value": "OFF",
                "Param": "query_cache_type",
                "Constraint": {
                    "Enum": "OFF,ON,DEMAND",
                    "Type": "enum"
                }
            },
            {
                "Default": "8192",
                "SetValue": "",
                "Value": "24576",
                "Param": "query_prealloc_size",
                "Constraint": {
                    "Range": {
                        "Max": "1048576",
                        "Min": "8192"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "10",
                "SetValue": "",
                "Value": "",
                "Param": "slave_parallel_threads",
                "Constraint": {
                    "Range": {
                        "Max": "16383",
                        "Min": "0"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "2",
                "SetValue": "",
                "Value": "2",
                "Param": "slow_launch_time",
                "Constraint": {
                    "Range": {
                        "Max": "1024",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "2097152",
                "SetValue": "",
                "Value": "2097152",
                "Param": "sort_buffer_size",
                "Constraint": {
                    "Range": {
                        "Max": "1073741824",
                        "Min": "32768"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "",
                "SetValue": "",
                "Value": "NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES",
                "Param": "sql_mode",
                "Constraint": {
                    "Type": "string"
                }
            },
            {
                "Default": "10",
                "SetValue": "",
                "Value": "30",
                "Param": "sqlasyntimeout",
                "Constraint": {
                    "Range": {
                        "Max": "100",
                        "Min": "10"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "400",
                "SetValue": "",
                "Value": "400",
                "Param": "table_definition_cache",
                "Constraint": {
                    "Range": {
                        "Max": "2048",
                        "Min": "400"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "1024",
                "SetValue": "",
                "Value": "10240",
                "Param": "table_open_cache",
                "Constraint": {
                    "Range": {
                        "Max": "524288",
                        "Min": "400"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "3",
                "SetValue": "",
                "Value": "30",
                "Param": "thread_pool_oversubscribe",
                "Constraint": {
                    "Range": {
                        "Max": "65536",
                        "Min": "1"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "33554432",
                "SetValue": "",
                "Value": "33554432",
                "Param": "tmp_table_size",
                "Constraint": {
                    "Range": {
                        "Max": "67108864",
                        "Min": "262144"
                    },
                    "Type": "section"
                }
            },
            {
                "Default": "REPEATABLE-READ",
                "SetValue": "",
                "Value": "REPEATABLE-READ",
                "Param": "tx_isolation",
                "Constraint": {
                    "Enum": "REPEATABLE-READ,SERIALIZABLE,READ-COMMITTED,READ-UNCOMMITTED",
                    "Type": "enum"
                }
            },
            {
                "Default": "28800",
                "SetValue": "",
                "Value": "28800",
                "Param": "wait_timeout",
                "Constraint": {
                    "Range": {
                        "Max": "259200",
                        "Min": "60"
                    },
                    "Type": "section"
                }
            }
        ],
        "RequestId": "914db412-d6e6-47ad-8e62-d06e02e52a56"
    }
}
```

