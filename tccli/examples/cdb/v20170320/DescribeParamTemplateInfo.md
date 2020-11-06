**Example 1: 查询参数模板详情**



Input: 

```
tccli cdb DescribeParamTemplateInfo --cli-unfold-argument  \
    --TemplateId 233
```

Output: 
```
{
    "Response": {
        "TemplateId": 233,
        "Name": "test",
        "EngineVersion": "5.7",
        "Description": "test",
        "TotalCount": 72,
        "Items": [
            {
                "Name": "max_connections",
                "ParamType": "integer",
                "Default": "151",
                "Description": "The maximum permitted number of simultaneous client connections.",
                "CurrentValue": "800",
                "NeedReboot": 0,
                "Max": 10240,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "character_set_server",
                "ParamType": "enum",
                "Default": "utf8",
                "Description": "Specify default server character set.",
                "CurrentValue": "utf8",
                "NeedReboot": 1,
                "EnumValue": [
                    "utf8",
                    "utf8mb4",
                    "gbk",
                    "latin1"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "lower_case_table_names",
                "ParamType": "integer",
                "Default": "0",
                "Description": "If set to 0, table names are stored as specified and comparisons are case sensitive. If set to 1, they are stored in lowercase on disk and comparisons are not case sensitive.",
                "CurrentValue": "0",
                "NeedReboot": 1,
                "Max": 1,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "wait_timeout",
                "ParamType": "integer",
                "Default": "7200",
                "Description": "The number of seconds the server waits for activity on a noninteractive connection before closing it.",
                "CurrentValue": "3600",
                "NeedReboot": 0,
                "Max": 7200,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "sql_mode",
                "ParamType": "enum",
                "Default": "ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION",
                "Description": "The current server SQL mode.",
                "CurrentValue": "REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ONLY_FULL_GROUP_BY,NO_UNSIGNED_SUBTRACTION,NO_DIR_IN_CREATE,NO_KEY_OPTIONS,NO_TABLE_OPTIONS,NO_FIELD_OPTIONS,NO_AUTO_VALUE_ON_ZERO,STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,HIGH_NOT_PRECEDENCE,NO_ENGINE_SUBSTITUTION,PAD_CHAR_TO_FULL_LENGTH",
                "NeedReboot": 0,
                "EnumValue": [
                    "",
                    "ALLOW_INVALID_DATES",
                    "ANSI_QUOTES",
                    "ERROR_FOR_DIVISION_BY_ZERO",
                    "HIGH_NOT_PRECEDENCE",
                    "IGNORE_SPACE",
                    "NO_AUTO_CREATE_USER",
                    "NO_AUTO_VALUE_ON_ZERO",
                    "NO_BACKSLASH_ESCAPES",
                    "NO_DIR_IN_CREATE",
                    "NO_ENGINE_SUBSTITUTION",
                    "NO_FIELD_OPTIONS",
                    "NO_KEY_OPTIONS",
                    "NO_TABLE_OPTIONS",
                    "NO_UNSIGNED_SUBTRACTION",
                    "NO_ZERO_DATE",
                    "NO_ZERO_IN_DATE",
                    "ONLY_FULL_GROUP_BY",
                    "PAD_CHAR_TO_FULL_LENGTH",
                    "PIPES_AS_CONCAT",
                    "REAL_AS_FLOAT",
                    "STRICT_ALL_TABLES",
                    "STRICT_TRANS_TABLES"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "binlog_row_image",
                "ParamType": "enum",
                "Default": "FULL",
                "Description": "Controls what formats that rows should be logged in.",
                "CurrentValue": "MINIMAL",
                "NeedReboot": 0,
                "EnumValue": [
                    "FULL",
                    "MINIMAL"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "table_open_cache",
                "ParamType": "integer",
                "Default": "2000",
                "Description": "The number of open tables for all threads. Increasing this value increases the number of file descriptors that mysqld requires.",
                "CurrentValue": "512",
                "NeedReboot": 0,
                "Max": 524288,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_open_files",
                "ParamType": "integer",
                "Default": "1024",
                "Description": "It specifies the maximum number of .ibd files that MySQL can keep open at one time.",
                "CurrentValue": "8192",
                "NeedReboot": 1,
                "Max": 8192,
                "Min": 10,
                "EnumValue": []
            },
            {
                "Name": "log_queries_not_using_indexes",
                "ParamType": "enum",
                "Default": "OFF",
                "Description": "Whether queries that do not use indexes are logged to the slow query log.",
                "CurrentValue": "OFF",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "table_definition_cache",
                "ParamType": "integer",
                "Default": "768",
                "Description": "The number of table definitions (from .frm files) that can be stored in the definition cache.",
                "CurrentValue": "4048",
                "NeedReboot": 0,
                "Max": 4048,
                "Min": 400,
                "EnumValue": []
            },
            {
                "Name": "event_scheduler",
                "ParamType": "enum",
                "Default": "OFF",
                "Description": "This variable indicates the status of the Event Scheduler.",
                "CurrentValue": "ON",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "tx_isolation",
                "ParamType": "enum",
                "Default": "REPEATABLE-READ",
                "Description": "Default transaction isolation level.",
                "CurrentValue": "READ-COMMITTED",
                "NeedReboot": 0,
                "EnumValue": [
                    "READ-COMMITTED",
                    "REPEATABLE-READ"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "innodb_autoinc_lock_mode",
                "ParamType": "integer",
                "Default": "1",
                "Description": "The lock mode to use for generating auto-increment values.",
                "CurrentValue": "0",
                "NeedReboot": 1,
                "Max": 2,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "innodb_flush_log_at_trx_commit",
                "ParamType": "integer",
                "Default": "1",
                "Description": "Controls the balance between strict ACID compliance for commit operations, and higher performance that is possible when commit-related I/O operations are rearranged and done in batches.",
                "CurrentValue": "2",
                "NeedReboot": 0,
                "Max": 2,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "sync_binlog",
                "ParamType": "integer",
                "Default": "1",
                "Description": "Controls the number of binary log commit groups to collect before synchronizing the binary log to disk.",
                "CurrentValue": "1",
                "NeedReboot": 0,
                "Max": 4294967295,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "tmp_table_size",
                "ParamType": "integer",
                "Default": "16777216",
                "Description": "The maximum size of internal in-memory temporary tables. This variable does not apply to user-created MEMORY tables.",
                "CurrentValue": "4194304",
                "NeedReboot": 0,
                "Max": 1073741824,
                "Min": 1024,
                "EnumValue": []
            },
            {
                "Name": "net_read_timeout",
                "ParamType": "integer",
                "Default": "30",
                "Description": "The number of seconds to wait for more data from a connection before aborting the read.",
                "CurrentValue": "31536000",
                "NeedReboot": 0,
                "Max": 31536000,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_lock_wait_timeout",
                "ParamType": "integer",
                "Default": "7200",
                "Description": "The length of time in seconds an InnoDB transaction waits for a row lock before giving up",
                "CurrentValue": "1073741824",
                "NeedReboot": 0,
                "Max": 1073741824,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "low_priority_updates",
                "ParamType": "enum",
                "Default": "OFF",
                "Description": "If set to true, all INSERT, UPDATE, DELETE, and LOCK TABLE WRITE statements wait until there is no pending SELECT or LOCK TABLE READ on the affected table",
                "CurrentValue": "ON",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "innodb_ft_max_token_size",
                "ParamType": "integer",
                "Default": "84",
                "Description": "Maximum character length of words that are stored in an InnoDB FULLTEXT index.",
                "CurrentValue": "64",
                "NeedReboot": 1,
                "Max": 84,
                "Min": 10,
                "EnumValue": []
            },
            {
                "Name": "delayed_queue_size",
                "ParamType": "integer",
                "Default": "1000",
                "Description": "What size queue (in rows) should be allocated for handling INSERT DELAYED. If the queue becomes full, any client that does INSERT DELAYED will wait until there is room in the queue again.",
                "CurrentValue": "4294967295",
                "NeedReboot": 0,
                "Max": 4294967295,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_ft_min_token_size",
                "ParamType": "integer",
                "Default": "3",
                "Description": "Minimum length of words that are stored in an InnoDB FULLTEXT index.",
                "CurrentValue": "16",
                "NeedReboot": 1,
                "Max": 16,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "innodb_old_blocks_time",
                "ParamType": "integer",
                "Default": "1000",
                "Description": "Specifies the approximate percentage of the InnoDB buffer pool used for the old block sublist",
                "CurrentValue": "2147483647",
                "NeedReboot": 0,
                "Max": 2147483647,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "myisam_sort_buffer_size",
                "ParamType": "integer",
                "Default": "8388608",
                "Description": "The size of the buffer that is allocated when sorting MyISAM indexes during a REPAIR TABLE or when creating indexes with CREATE INDEX or ALTER TABLE",
                "CurrentValue": "524288",
                "NeedReboot": 0,
                "Max": 16777216,
                "Min": 262144,
                "EnumValue": []
            },
            {
                "Name": "net_retry_count",
                "ParamType": "integer",
                "Default": "10",
                "Description": "If a read or write on a communication port is interrupted, retry this many times before giving up.",
                "CurrentValue": "4294967295",
                "NeedReboot": 0,
                "Max": 4294967295,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "max_user_connections",
                "ParamType": "integer",
                "Default": "0",
                "Description": "The maximum permitted number of simultaneous client connections per user.",
                "CurrentValue": "10240",
                "NeedReboot": 0,
                "Max": 10240,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "max_length_for_sort_data",
                "ParamType": "integer",
                "Default": "1024",
                "Description": "The cutoff on the size of index values that determines which filesort algorithm to use.",
                "CurrentValue": "8388608",
                "NeedReboot": 0,
                "Max": 8388608,
                "Min": 4,
                "EnumValue": []
            },
            {
                "Name": "innodb_write_io_threads",
                "ParamType": "integer",
                "Default": "4",
                "Description": "The number of I/O threads for write operations in InnoDB.",
                "CurrentValue": "64",
                "NeedReboot": 1,
                "Max": 64,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "delay_key_write",
                "ParamType": "enum",
                "Default": "ON",
                "Description": "This option applies only to MyISAM tables. It can have one of the following values to affect handling of the DELAY_KEY_WRITE table option that can be used in CREATE TABLE statements.",
                "CurrentValue": "ALL",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF",
                    "ALL"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "query_prealloc_size",
                "ParamType": "integer",
                "Default": "8192",
                "Description": "The size of the persistent buffer used for statement parsing and execution. This buffer is not freed between statements.",
                "CurrentValue": "1048576",
                "NeedReboot": 0,
                "Max": 1048576,
                "Min": 8192,
                "EnumValue": []
            },
            {
                "Name": "innodb_strict_mode",
                "ParamType": "enum",
                "Default": "OFF",
                "Description": "When innodb_strict_mode is ON, InnoDB returns errors rather than warnings for certain conditions",
                "CurrentValue": "ON",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "max_connect_errors",
                "ParamType": "integer",
                "Default": "100",
                "Description": "If more than this many successive connection requests from a host are interrupted without a successful connection, the server blocks that host from further connections.",
                "CurrentValue": "999999999",
                "NeedReboot": 0,
                "Max": 4294967295,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "concurrent_insert",
                "ParamType": "enum",
                "Default": "AUTO",
                "Description": "If AUTO (the default), MySQL permits INSERT and SELECT statements to run concurrently for MyISAM tables that have no free blocks in the middle of the data file.",
                "CurrentValue": "NEVER",
                "NeedReboot": 0,
                "EnumValue": [
                    "NEVER",
                    "AUTO",
                    "ALWAYS"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "innodb_old_blocks_pct",
                "ParamType": "integer",
                "Default": "37",
                "Description": "Specifies the approximate percentage of the InnoDB buffer pool used for the old block sublist",
                "CurrentValue": "95",
                "NeedReboot": 0,
                "Max": 95,
                "Min": 5,
                "EnumValue": []
            },
            {
                "Name": "auto_increment_offset",
                "ParamType": "integer",
                "Default": "1",
                "Description": "Determines the starting point for the AUTO_INCREMENT column value.",
                "CurrentValue": "65535",
                "NeedReboot": 0,
                "Max": 65535,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_read_io_threads",
                "ParamType": "integer",
                "Default": "4",
                "Description": "The number of I/O threads for read operations in InnoDB.",
                "CurrentValue": "64",
                "NeedReboot": 1,
                "Max": 64,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "thread_cache_size",
                "ParamType": "integer",
                "Default": "512",
                "Description": "How many threads we should keep in a cache for reuse",
                "CurrentValue": "128",
                "NeedReboot": 0,
                "Max": 1000,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "default_week_format",
                "ParamType": "integer",
                "Default": "0",
                "Description": "The default mode value to use for the WEEK() function",
                "CurrentValue": "7",
                "NeedReboot": 0,
                "Max": 7,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "ft_query_expansion_limit",
                "ParamType": "integer",
                "Default": "20",
                "Description": "Number of best matches to use for query expansion",
                "CurrentValue": "1000",
                "NeedReboot": 1,
                "Max": 1000,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "delayed_insert_limit",
                "ParamType": "integer",
                "Default": "100",
                "Description": "After inserting delayed_insert_limit rows, the INSERT DELAYED handler will check if there are any SELECT statements pending. If so, it allows these to execute before continuing.",
                "CurrentValue": "4294967295",
                "NeedReboot": 0,
                "Max": 4294967295,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "group_concat_max_len",
                "ParamType": "integer",
                "Default": "1024",
                "Description": "The maximum permitted result length in bytes for the GROUP_CONCAT() function",
                "CurrentValue": "4294967295",
                "NeedReboot": 0,
                "Max": 4294967295,
                "Min": 4,
                "EnumValue": []
            },
            {
                "Name": "innodb_thread_sleep_delay",
                "ParamType": "integer",
                "Default": "0",
                "Description": "How long InnoDB threads sleep before joining the InnoDB queue, in microseconds. ",
                "CurrentValue": "10000",
                "NeedReboot": 0,
                "Max": 1000000,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "key_cache_age_threshold",
                "ParamType": "integer",
                "Default": "300",
                "Description": "This characterizes the number of hits a hot block has to be untouched until it is considered aged enough to be downgraded to a warm block. This specifies the percentage ratio of that number of hits to the total number of blocks in key cache.",
                "CurrentValue": "300",
                "NeedReboot": 0,
                "Max": 4294967295,
                "Min": 100,
                "EnumValue": []
            },
            {
                "Name": "innodb_concurrency_tickets",
                "ParamType": "integer",
                "Default": "5000",
                "Description": "Determines the number of threads that can enter InnoDB concurrently",
                "CurrentValue": "5000",
                "NeedReboot": 0,
                "Max": 4294967295,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_read_ahead_threshold",
                "ParamType": "integer",
                "Default": "56",
                "Description": "Controls the sensitivity of linear read-ahead that InnoDB uses to prefetch pages into the buffer pool",
                "CurrentValue": "56",
                "NeedReboot": 0,
                "Max": 64,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "innodb_max_dirty_pages_pct",
                "ParamType": "float",
                "Default": "75",
                "Description": "InnoDB tries to flush data from the buffer pool so that the percentage of dirty pages does not exceed this value",
                "CurrentValue": "75.000000",
                "NeedReboot": 0,
                "Max": 99,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "connect_timeout",
                "ParamType": "integer",
                "Default": "10",
                "Description": "The number of seconds that the mysqld server waits for a connect packet before responding with Bad handshake",
                "CurrentValue": "1800",
                "NeedReboot": 0,
                "Max": 1800,
                "Min": 2,
                "EnumValue": []
            },
            {
                "Name": "log_timestamps",
                "ParamType": "enum",
                "Default": "UTC",
                "Description": "This variable controls the time zone of timestamps in messages written to the error log, and in general query log and slow query log messages written to files.",
                "CurrentValue": "SYSTEM",
                "NeedReboot": 0,
                "EnumValue": [
                    "UTC",
                    "SYSTEM"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "ft_min_word_len",
                "ParamType": "integer",
                "Default": "4",
                "Description": "The minimum length of the word to be included in a FULLTEXT index. Note: FULLTEXT indexes must be rebuilt after changing this variable.",
                "CurrentValue": "84",
                "NeedReboot": 1,
                "Max": 84,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "ngram_token_size",
                "ParamType": "integer",
                "Default": "2",
                "Description": "ngram_token_size is set to the size of the largest token that you want to search for.",
                "CurrentValue": "1",
                "NeedReboot": 1,
                "Max": 10,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "auto_increment_increment",
                "ParamType": "integer",
                "Default": "1",
                "Description": "Controls the interval between successive column values.",
                "CurrentValue": "65535",
                "NeedReboot": 0,
                "Max": 65535,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "key_cache_division_limit",
                "ParamType": "integer",
                "Default": "100",
                "Description": "The minimum percentage of warm blocks in key cache",
                "CurrentValue": "100",
                "NeedReboot": 0,
                "Max": 100,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "div_precision_increment",
                "ParamType": "integer",
                "Default": "4",
                "Description": "This variable indicates the number of digits by which to increase the scale of the result of division operations performed with the operator",
                "CurrentValue": "4",
                "NeedReboot": 0,
                "Max": 30,
                "Min": 0,
                "EnumValue": []
            },
            {
                "Name": "innodb_table_locks",
                "ParamType": "enum",
                "Default": "ON",
                "Description": "If autocommit = 0, InnoDB honors LOCK TABLES; MySQL does not return from LOCK TABLES ... WRITE until all other threads have released all their locks to the table. The default value of innodb_table_locks is 1, which means that LOCK TABLES causes InnoDB to lock a table internally if autocommit = 0.",
                "CurrentValue": "OFF",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "lock_wait_timeout",
                "ParamType": "integer",
                "Default": "31536000",
                "Description": "his variable specifies the timeout in seconds for attempts to acquire metadata locks.",
                "CurrentValue": "31536000",
                "NeedReboot": 0,
                "Max": 31536000,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_ft_enable_stopword",
                "ParamType": "enum",
                "Default": "ON",
                "Description": "Create FTS index with stopword.",
                "CurrentValue": "ON",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "net_write_timeout",
                "ParamType": "integer",
                "Default": "60",
                "Description": "The number of seconds to wait for a block to be written to a connection before aborting the write.",
                "CurrentValue": "60",
                "NeedReboot": 0,
                "Max": 31536000,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_print_all_deadlocks",
                "ParamType": "enum",
                "Default": "OFF",
                "Description": "When this option is enabled, information about all deadlocks in InnoDB user transactions is recorded in the mysqld error log.",
                "CurrentValue": "ON",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "query_alloc_block_size",
                "ParamType": "integer",
                "Default": "8192",
                "Description": "The allocation size of memory blocks that are allocated for objects created during statement parsing and execution.",
                "CurrentValue": "2048",
                "NeedReboot": 0,
                "Max": 16384,
                "Min": 1024,
                "EnumValue": []
            },
            {
                "Name": "query_cache_wlock_invalidate",
                "ParamType": "enum",
                "Default": "OFF",
                "Description": "Invalidate queries in query cache on LOCK for write",
                "CurrentValue": "ON",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "innodb_adaptive_hash_index",
                "ParamType": "enum",
                "Default": "ON",
                "Description": "Whether the InnoDB adaptive hash index is enabled or disabled.",
                "CurrentValue": "OFF",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "performance_schema",
                "ParamType": "enum",
                "Default": "OFF",
                "Description": "Whether enable the performance schema.",
                "CurrentValue": "ON",
                "NeedReboot": 1,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "delayed_insert_timeout",
                "ParamType": "integer",
                "Default": "300",
                "Description": "How long a INSERT DELAYED thread should wait for INSERT statements before terminating.",
                "CurrentValue": "3600",
                "NeedReboot": 0,
                "Max": 3600,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_purge_batch_size",
                "ParamType": "integer",
                "Default": "300",
                "Description": "The granularity of changes, expressed in units of redo log records, that trigger a purge operation, flushing the changed buffer pool blocks to disk.",
                "CurrentValue": "5000",
                "NeedReboot": 0,
                "Max": 5000,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "slow_launch_time",
                "ParamType": "integer",
                "Default": "2",
                "Description": "If creating a thread takes longer than this many seconds, the server increments the Slow_launch_threads status variable",
                "CurrentValue": "10",
                "NeedReboot": 0,
                "Max": 10,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_purge_threads",
                "ParamType": "integer",
                "Default": "1",
                "Description": "The number of background threads devoted to the InnoDB purge operation.",
                "CurrentValue": "16",
                "NeedReboot": 1,
                "Max": 32,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_large_prefix",
                "ParamType": "enum",
                "Default": "OFF",
                "Description": "Enable this option to allow index key prefixes longer than 767 bytes (up to 3072 bytes) for InnoDB tables that use the DYNAMIC and COMPRESSED row formats.",
                "CurrentValue": "ON",
                "NeedReboot": 0,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "table_open_cache_instances",
                "ParamType": "integer",
                "Default": "16",
                "Description": "The number of table cache instances",
                "CurrentValue": "64",
                "NeedReboot": 1,
                "Max": 64,
                "Min": 1,
                "EnumValue": []
            },
            {
                "Name": "innodb_online_alter_log_max_size",
                "ParamType": "integer",
                "Default": "134217728",
                "Description": "Maximum modification log file size for online index creation",
                "CurrentValue": "2147483647",
                "NeedReboot": 0,
                "Max": 2147483647,
                "Min": 134217728,
                "EnumValue": []
            },
            {
                "Name": "innodb_rollback_on_timeout",
                "ParamType": "enum",
                "Default": "OFF",
                "Description": "InnoDB rolls back only the last statement on a transaction timeout by default. If innodb_rollback_on_timeout is specified, a transaction timeout causes InnoDB to abort and roll back the entire transaction.",
                "CurrentValue": "ON",
                "NeedReboot": 1,
                "EnumValue": [
                    "ON",
                    "OFF"
                ],
                "Max": 0,
                "Min": 0
            },
            {
                "Name": "key_cache_block_size",
                "ParamType": "integer",
                "Default": "1024",
                "Description": "The default size of key cache blocks",
                "CurrentValue": "4096",
                "NeedReboot": 0,
                "Max": 16384,
                "Min": 512,
                "EnumValue": []
            },
            {
                "Name": "eq_range_index_dive_limit",
                "ParamType": "integer",
                "Default": "10",
                "Description": "The optimizer will use existing index statistics instead of doing index dives for equality ranges if the number of equality ranges for the index is larger than or equal to this number. If set to 0, index dives are always used.",
                "CurrentValue": "1",
                "NeedReboot": 0,
                "Max": 200,
                "Min": 1,
                "EnumValue": []
            }
        ],
        "RequestId": "92131c95-aa65-44db-8c3c-e8cd67883b58"
    }
}
```

