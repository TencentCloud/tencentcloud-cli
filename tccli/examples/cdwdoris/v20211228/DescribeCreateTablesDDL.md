**Example 1: 获取建表ddl**

获取建表ddl

Input: 

```
tccli cdwdoris DescribeCreateTablesDDL --cli-unfold-argument  \
    --InstanceId cdwdoris-bjizjxxx \
    --DbTablesInfos.0.DbName demo1 \
    --DbTablesInfos.0.TablesName unique_idx_col13 \
    --DbTablesInfos.1.DbName demo2 \
    --DbTablesInfos.1.TablesName duplicate_list_partition
```

Output: 
```
{
    "Response": {
        "CreateTablesDDLs": [
            {
                "DbName": "demo1",
                "TablesDDLs": [
                    {
                        "DDLInfo": "CREATE TABLE `unique_idx_col13` (\n  `user_id` LARGEINT NOT NULL COMMENT '用户id',\n  `date` DATE NOT NULL COMMENT '数据导入日期时间',\n  `city` VARCHAR(20) NULL COMMENT '用户所在城市',\n  `age` SMALLINT NULL COMMENT '用户年龄',\n  `sex` TINYINT NULL COMMENT '用户性别',\n  `f6_decimal` DECIMAL(10, 6) NULL COMMENT 'DECIMAL列',\n  `f7_boolean` BOOLEAN NULL COMMENT 'BOOLEAN列 0代表false，1代表true',\n  `f8_double` DOUBLE NULL COMMENT 'DOUBLE列',\n  `f9_float` FLOAT NULL COMMENT 'FLOAT列',\n  `f10_string` TEXT NULL COMMENT 'STRING列',\n  `last_visit_date` DATETIME NULL COMMENT '用户最后一次访问时间',\n  `cost` BIGINT NULL COMMENT '用户总消费，默认0',\n  `max_dwell_time` INT NULL COMMENT '用户最大停留时间,默认0'\n) ENGINE=OLAP\nUNIQUE KEY(`user_id`, `date`, `city`)\nDISTRIBUTED BY HASH(`user_id`) BUCKETS 1\nPROPERTIES (\n\"replication_allocation\" = \"tag.location.default: 1\",\n\"min_load_replica_num\" = \"-1\",\n\"is_being_synced\" = \"false\",\n\"storage_medium\" = \"hdd\",\n\"storage_format\" = \"V2\",\n\"inverted_index_storage_format\" = \"V1\",\n\"enable_unique_key_merge_on_write\" = \"true\",\n\"light_schema_change\" = \"true\",\n\"disable_auto_compaction\" = \"false\",\n\"enable_single_replica_compaction\" = \"false\",\n\"group_commit_interval_ms\" = \"10000\",\n\"group_commit_data_bytes\" = \"134217728\",\n\"enable_mow_light_delete\" = \"false\"\n);",
                        "TableName": "unique_idx_col13"
                    }
                ]
            },
            {
                "DbName": "demo2",
                "TablesDDLs": [
                    {
                        "DDLInfo": "CREATE TABLE `duplicate_list_partition` (\n  `user_id` LARGEINT NOT NULL COMMENT '用户id',\n  `date` DATE NOT NULL COMMENT '数据导入日期时间',\n  `city` VARCHAR(20) NOT NULL COMMENT '用户所在城市',\n  `age` SMALLINT NULL COMMENT '用户年龄',\n  `sex` TINYINT NULL COMMENT '用户性别',\n  `f6_decimal` DECIMAL(10, 6) NULL COMMENT 'DECIMAL列',\n  `f7_boolean` BOOLEAN NULL COMMENT 'BOOLEAN列 0代表false，1代表true',\n  `f8_double` DOUBLE NULL COMMENT 'DOUBLE列',\n  `f9_float` FLOAT NULL COMMENT 'FLOAT列',\n  `f10_string` TEXT NULL COMMENT 'STRING列',\n  `last_visit_date` DATETIME NULL COMMENT '用户最后一次访问时间',\n  `cost` BIGINT NULL COMMENT '用户总消费，默认0',\n  `max_dwell_time` INT NULL COMMENT '用户最大停留时间,默认0'\n) ENGINE=OLAP\nDUPLICATE KEY(`user_id`, `date`, `city`)\nPARTITION BY LIST(`city`)\n(PARTITION city_bj VALUES IN (\"Beijing\",\"beijing\",\"BEIJING\",\"BeiJing\",\"北京\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION city_cd VALUES IN (\"Chengdu\",\"chengdu\",\"CHENGDU\",\"ChengDu\",\"成都\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION city_sh VALUES IN (\"Shanghai\",\"shanghai\",\"SHANGHAI\",\"ShangHai\",\"上海\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p1 VALUES IN (\"haha1\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p10 VALUES IN (\"haha10\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p11 VALUES IN (\"haha11\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p12 VALUES IN (\"haha12\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p13 VALUES IN (\"haha13\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p14 VALUES IN (\"haha14\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p15 VALUES IN (\"haha15\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p16 VALUES IN (\"haha16\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p17 VALUES IN (\"haha17\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p18 VALUES IN (\"haha18\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p19 VALUES IN (\"haha19\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p2 VALUES IN (\"haha2\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p20 VALUES IN (\"haha20\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p21 VALUES IN (\"haha21\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p22 VALUES IN (\"haha22\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p23 VALUES IN (\"haha23\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p24 VALUES IN (\"haha24\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p25 VALUES IN (\"haha25\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p26 VALUES IN (\"haha26\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p27 VALUES IN (\"haha27\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p28 VALUES IN (\"haha28\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p29 VALUES IN (\"haha29\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p3 VALUES IN (\"haha3\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p30 VALUES IN (\"haha30\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p4 VALUES IN (\"haha4\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p5 VALUES IN (\"haha5\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p6 VALUES IN (\"haha6\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p7 VALUES IN (\"haha7\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p8 VALUES IN (\"haha8\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION add_p9 VALUES IN (\"haha9\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_0 VALUES IN (\"wuhan0\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_1 VALUES IN (\"wuhan1\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_10 VALUES IN (\"wuhan10\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_2 VALUES IN (\"wuhan2\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_3 VALUES IN (\"wuhan3\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_4 VALUES IN (\"wuhan4\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_5 VALUES IN (\"wuhan5\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_6 VALUES IN (\"wuhan6\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_7 VALUES IN (\"wuhan7\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_8 VALUES IN (\"wuhan8\") (\"storage_policy\" = \"20240806-16-48-降冷\"),\nPARTITION wh_partition_9 VALUES IN (\"wuhan9\") (\"storage_policy\" = \"20240806-16-48-降冷\"))\nDISTRIBUTED BY HASH(`user_id`) BUCKETS 1\nPROPERTIES (\n\"replication_allocation\" = \"tag.location.default: 3\",\n\"min_load_replica_num\" = \"-1\",\n\"is_being_synced\" = \"false\",\n\"storage_medium\" = \"hdd\",\n\"storage_format\" = \"V2\",\n\"inverted_index_storage_format\" = \"V1\",\n\"light_schema_change\" = \"true\",\n\"disable_auto_compaction\" = \"false\",\n\"enable_single_replica_compaction\" = \"false\",\n\"group_commit_interval_ms\" = \"10000\",\n\"group_commit_data_bytes\" = \"134217728\"\n);",
                        "TableName": "duplicate_list_partition"
                    }
                ]
            }
        ],
        "Message": "",
        "RequestId": "f8f5e0af-7d36-4b49-8b4d-9c103deef55a"
    }
}
```

