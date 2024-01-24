**Example 1: demo**



Input: 

```
tccli wedata DescribeCodeSearchInfo --cli-unfold-argument  \
    --SearchScope orchrestrationSpace \
    --PageSize 10 \
    --Keyword hannah \
    --SearchScopes orchrestrationSpace \
    --ProjectId 1 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4dbc8060-65c0-40d4-940a-9f0b979abfcd",
        "Data": {
            "CodeSearchInfoList": {
                "Rows": [
                    {
                        "Id": "20220331164614525",
                        "Name": "leilei1",
                        "Type": "26",
                        "Content": [
                            {
                                "Number": 1,
                                "Line": "[{\"title\":\"类型\",\"value\":\"MYSQL\"},{\"title\":\"数据库\",\"value\":\"hannah\"},{\"title\":\"表名\",\"value\":\"msg_record\"},{\"title\":\"字段名\",\"value\":\"attributes,card_type,card_value,gmt_create,gmt_modify,group_code,group_name,group_robot_id,id,is_delete,msg_content,msg_task_id,msg_type,result_message,result_status,robot_code,robot_nick,send_time,shopkeeper_cuser_id,sub_biz_type\"}]",
                                "NodeType": "INPUT"
                            }
                        ],
                        "OwnerName": "ryanrliao",
                        "UpdateTime": "2022-05-12 17:38:54",
                        "CreateTime": "2022-03-31 16:46:14",
                        "MatchRows": 1,
                        "DisplayType": "config"
                    },
                    {
                        "Id": "20220331165851020",
                        "Name": "copy_mysql2hive_20220331165851008",
                        "Type": "26",
                        "Content": [
                            {
                                "Number": 1,
                                "Line": "[{\"title\":\"类型\",\"value\":\"MYSQL\"},{\"title\":\"数据库\",\"value\":\"hannah\"},{\"title\":\"表名\",\"value\":\"msg_record\"},{\"title\":\"字段名\",\"value\":\"attributes,card_type,card_value,gmt_create,gmt_modify,group_code,group_name,group_robot_id,id,is_delete,msg_content,msg_task_id,msg_type,result_message,result_status,robot_code,robot_nick,send_time,shopkeeper_cuser_id,sub_biz_type\"}]",
                                "NodeType": "INPUT"
                            }
                        ],
                        "OwnerName": "ryanrliao",
                        "UpdateTime": "2022-04-14 12:23:07",
                        "CreateTime": "2022-03-31 16:58:51",
                        "MatchRows": 1,
                        "DisplayType": "config"
                    }
                ],
                "TotalCount": 2
            },
            "DevCount": 0,
            "ScheduleCount": 2,
            "RecycleCount": 0
        }
    }
}
```

