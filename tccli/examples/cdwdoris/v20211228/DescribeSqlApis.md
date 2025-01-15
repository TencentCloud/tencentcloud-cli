**Example 1: 获取数据库列表**



Input: 

```
tccli cdwdoris DescribeSqlApis --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3 \
    --ApiType GetDatabases \
    --Catalog internal
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "267b8c6c-d8ab-440c-bd01-7f060c76d572",
        "ReturnData": "[\"__internal_schema\",\"db_demo\",\"demo\",\"information_schema\",\"mysql\"]"
    }
}
```

**Example 2: 获取用户列表**



Input: 

```
tccli cdwdoris DescribeSqlApis --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3 \
    --ApiType GetUsers
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "5d704cb1-9cce-41b0-8841-c20318fad683",
        "ReturnData": "[{\"InstanceId\":\"cdwdoris-qliqegj3\",\"UserName\":\"admin\",\"WhiteHost\":\"\",\"Describe\":\"系统用户，权限不能修改，也不能删除\",\"GlobalPriList\":null},{\"InstanceId\":\"cdwdoris-qliqegj3\",\"UserName\":\"test\",\"WhiteHost\":\"%\",\"Describe\":\"\",\"GlobalPriList\":[\"ADMIN_PRIV\"]}]"
    }
}
```

**Example 3: 获取数据库表列表**



Input: 

```
tccli cdwdoris DescribeSqlApis --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3 \
    --ApiType GetTables \
    --Catalogs internal
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "4d1c7a4c-fd61-4537-a9f1-b377c9457f78",
        "ReturnData": "{\"internal\":[{\"DatabaseName\":\"information_schema\",\"Tables\":[\"table_constraints\",\"referential_constraints\",\"columns\",\"schemata\",\"column_privileges\",\"column_statistics\",\"parameters\",\"statistics\",\"profiling\",\"key_column_usage\",\"global_variables\",\"table_privileges\",\"user_privileges\",\"partitions\",\"collations\",\"triggers\",\"engines\",\"active_queries\",\"metadata_name_ids\",\"files\",\"catalog_meta_cache_statistics\",\"processlist\",\"events\",\"table_properties\",\"session_variables\",\"workload_group_resource_usage\",\"rowsets\",\"file_cache_statistics\",\"views\",\"character_sets\",\"workload_groups\",\"workload_policy\",\"workload_group_privileges\",\"routines\",\"schema_privileges\",\"tables\",\"table_options\",\"backend_active_tasks\"]},{\"DatabaseName\":\"demo\",\"Tables\":[\"add_table2\"]},{\"DatabaseName\":\"__internal_schema\",\"Tables\":[\"audit_log\",\"column_statistics\",\"histogram_statistics\"]},{\"DatabaseName\":\"mysql\",\"Tables\":[\"procs_priv\",\"user\"]},{\"DatabaseName\":\"db_demo\",\"Tables\":[]}]}"
    }
}
```

