**Example 1: 添加字段**

为 test_tbl 添加字段

Input: 

```
tccli dcdb CreateOnlineDDLJob --cli-unfold-argument  \
    --InstanceId tdsqlshard-h2yimmox \
    --Alter alter table test_tbl add column test_add_col  varchar(32) not null default 'test' comment 'test add col'; \
    --DbName test_db \
    --Table test_tbl \
    --CriticalLoad 58 \
    --CheckAutoInc 0 \
    --MaxDelay 10 \
    --UsePt 1 \
    --User test_user \
    --Password test_pwd \
    --StartTime 
```

Output: 
```
{
    "Response": {
        "FlowId": 1140696,
        "RequestId": "bd07e59f-dee8-4680-9a43-492a8a52c894"
    }
}
```

**Example 2: 添加索引**

为 test_tbl添加索引
添加唯一索引 ：alter table test_tbl add unique key my_idx(id,name); 
添加普通索引：alter table test_tbl add key my_idx_1(id,name); 

Input: 

```
tccli dcdb CreateOnlineDDLJob --cli-unfold-argument  \
    --InstanceId tdsql-4z38cfwj \
    --Alter alter table test_tbl add unique key my_idx(id,name);  \
    --DbName test_db \
    --Table test_tbl \
    --CriticalLoad 58 \
    --CheckAutoInc 0 \
    --MaxDelay 10 \
    --UsePt 1 \
    --User test_user \
    --Password test_pwd \
    --StartTime 
```

Output: 
```
{
    "Response": {
        "FlowId": 1140697,
        "RequestId": "c5afb15f-70c8-4e71-84b5-688dd326a8c3"
    }
}
```

**Example 3: 删除字段**

从test_tbl删除字段 test_add_col 

Input: 

```
tccli dcdb CreateOnlineDDLJob --cli-unfold-argument  \
    --InstanceId tdsqlshard-h2yimmox \
    --Alter alter table test_tbl drop column test_add_col;  \
    --DbName test_db \
    --Table test_tbl \
    --CriticalLoad 58 \
    --CheckAutoInc 0 \
    --MaxDelay 10 \
    --UsePt 1 \
    --User test_user \
    --Password test_pwd \
    --StartTime 
```

Output: 
```
{
    "Response": {
        "FlowId": 1140698,
        "RequestId": "a9f824be-fc53-41f7-9e24-2aca60457331"
    }
}
```

**Example 4: 修改字段**

将 test_tbl 表字段 test_add_col 从varchar(32) 修改为 varchar(64)

Input: 

```
tccli dcdb CreateOnlineDDLJob --cli-unfold-argument  \
    --InstanceId tdsqlshard-h2yimmox \
    --Alter alter table test_tbl modify column test_add_col varchar(64) not null default 'test' comment 'test change type';  \
    --DbName test_db \
    --Table test_tbl \
    --CriticalLoad 58 \
    --CheckAutoInc 0 \
    --MaxDelay 10 \
    --UsePt 1 \
    --User test_user \
    --Password test_pwd \
    --StartTime 
```

Output: 
```
{
    "Response": {
        "FlowId": 1140699,
        "RequestId": "7e2e0512-e429-4702-a9a6-d920eebd6536"
    }
}
```

**Example 5: 表空间优化**

表空间优化

Input: 

```
tccli dcdb CreateOnlineDDLJob --cli-unfold-argument  \
    --InstanceId tdsqlshard-h2yimmox \
    --Alter alter table test_tbl engine=innodb;  \
    --DbName test_db \
    --Table test_tbl \
    --CriticalLoad 58 \
    --CheckAutoInc 0 \
    --MaxDelay 10 \
    --UsePt 1 \
    --User test_user \
    --Password test_pwd \
    --StartTime 
```

Output: 
```
{
    "Response": {
        "FlowId": 1140701,
        "RequestId": "9df10ff7-9db5-4cad-81e2-3ad742f7bc06"
    }
}
```

