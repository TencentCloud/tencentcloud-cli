**Example 1: 查询血缘**

查询血缘

Input: 

```
tccli wedata DescribeLineageInfo --cli-unfold-argument  \
    --ResourceOriId guid_of_table \
    --ResourceType TABLE \
    --Direction BOTH \
    --InputDepth 3 \
    --OutputDepth 3 \
    --Platform WEDATA \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "req_id_***",
        "Data": {
            "CurrentResource": {
                "ResourceOriId": "guid_of_table",
                "ResourceName": "dwd_example_table",
                "ResourceType": "TABLE",
                "QualifiedId": "wedata::TABLE::guid_of_table",
                "Description": "示例表",
                "Platform": "WEDATA",
                "CreateTime": "2026-01-15 10:30:00",
                "UpdateTime": "2026-03-10 14:20:00",
                "ResourceProperties": [
                    {
                        "Name": "databaseName",
                        "Value": "dwd"
                    },
                    {
                        "Name": "dataSourceType",
                        "Value": "HIVE"
                    },
                    {
                        "Name": "dataSourceName",
                        "Value": "hive_emr-***"
                    }
                ]
            },
            "ParentSet": [
                {
                    "CurrentResource": {
                        "ResourceOriId": "guid_upstream_1",
                        "ResourceName": "ods_raw_data",
                        "ResourceType": "TABLE",
                        "QualifiedId": "wedata::TABLE::guid_upstream_1",
                        "Platform": "WEDATA",
                        "ResourceProperties": [
                            {
                                "Name": "databaseName",
                                "Value": "ods"
                            },
                            {
                                "Name": "dataSourceType",
                                "Value": "HIVE"
                            }
                        ]
                    },
                    "Relation": {
                        "RelationId": "rel_001",
                        "SourceQualifiedId": "wedata::TABLE::guid_upstream_1",
                        "TargetQualifiedId": "wedata::TABLE::guid_of_table",
                        "Processes": [
                            {
                                "ProcessId": "task_12345",
                                "ProcessType": "DATA_INTEGRATION",
                                "ProcessName": "dwd_example_etl",
                                "QualifiedId": "wedata::TASK::task_12345",
                                "Platform": "WEDATA"
                            }
                        ]
                    },
                    "ParentSet": [],
                    "ChildSet": [],
                    "UpStreamCount": 0,
                    "DownStreamCount": 0
                }
            ],
            "ChildSet": [
                {
                    "CurrentResource": {
                        "ResourceOriId": "guid_downstream_1",
                        "ResourceName": "ads_report_daily",
                        "ResourceType": "TABLE",
                        "QualifiedId": "wedata::TABLE::guid_downstream_1",
                        "Platform": "WEDATA",
                        "ResourceProperties": [
                            {
                                "Name": "databaseName",
                                "Value": "ads"
                            },
                            {
                                "Name": "dataSourceType",
                                "Value": "HIVE"
                            }
                        ]
                    },
                    "Relation": {
                        "RelationId": "rel_002",
                        "SourceQualifiedId": "wedata::TABLE::guid_of_table",
                        "TargetQualifiedId": "wedata::TABLE::guid_downstream_1",
                        "Processes": [
                            {
                                "ProcessId": "task_67890",
                                "ProcessType": "HIVE_SQL",
                                "ProcessName": "ads_daily_report_job",
                                "QualifiedId": "wedata::TASK::task_67890",
                                "Platform": "WEDATA"
                            }
                        ]
                    },
                    "ParentSet": [],
                    "ChildSet": [],
                    "UpStreamCount": 0,
                    "DownStreamCount": 2
                }
            ],
            "UpStreamCount": 1,
            "DownStreamCount": 1,
            "StreamCountFlag": false
        }
    }
}
```

