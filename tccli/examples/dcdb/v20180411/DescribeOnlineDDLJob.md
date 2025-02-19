**Example 1: 查询OnlineDDL任务详情**



Input: 

```
tccli dcdb DescribeOnlineDDLJob --cli-unfold-argument  \
    --InstanceId tdsqlshard-a2csrmsr \
    --FlowId 1143769
```

Output: 
```
{
    "Response": {
        "DDLDetails": [
            {
                "Alter": "add column add_col1;",
                "BeginTime": "2025-01-16 16:26:15 +0800 CST",
                "DbName": "db_prod",
                "Desc": "Error Error altering new table `db_prod`.`_tbl_user_new`: DBD::mysql::db do failed: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1 [for Statement \"ALTER TABLE `db_prod`.`_tbl_user_new` add column add_col1;\"] at ./pt-online-schema-change line 9121.\n",
                "ShardSerialId": "set_1734351063_1",
                "Stage": "before_alter_new_table",
                "Status": 1,
                "SwitchStatus": 0,
                "Table": "tbl_user"
            }
        ],
        "ErrorMessage": "Error Error altering new table `db_prod`.`_tbl_user_new`: DBD::mysql::db do failed: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1 [for Statement \"ALTER TABLE `db_prod`.`_tbl_user_new` add column add_col1;\"] at ./pt-online-schema-change line 9121.\n",
        "Process": 100,
        "RequestId": "9524d8fa-8598-414a-a3a1-4134c9631ca2",
        "Status": 1
    }
}
```

