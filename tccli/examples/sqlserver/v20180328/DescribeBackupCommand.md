**Example 1: 查询创建全量备份的命令**



Input: 

```
tccli sqlserver DescribeBackupCommand --cli-unfold-argument  \
    --BackupFileType FULL \
    --DataBaseName db1 \
    --IsRecovery YES \
    --LocalPath E:/
```

Output: 
```
{
    "Response": {
        "Command": "BACKUP DATABASE db1 TO DISK='E:/db1.bak' WITH INIT",
        "RequestId": "1de3aea3-5fef-4891-b8b0-faeb4e3b5543"
    }
}
```

**Example 2: 查询创建日志增量的命令**

在需要事务日志做增量导入时使用，此时获取的是恢复的事务日志增量备份。
命令中\\\\n为换行符。

Input: 

```
tccli sqlserver DescribeBackupCommand --cli-unfold-argument  \
    --BackupFileType LOG \
    --DataBaseName db1 \
    --IsRecovery YES \
    --LocalPath E:/
```

Output: 
```
{
    "Response": {
        "Command": "declare @dbname varchar(100)\\\\ndeclare @localtime varchar(20)\\\\ndeclare @str varchar(8000)\\\\nset @dbname='db1'\\\\nset @localtime =replace(replace(replace(CONVERT(varchar, getdate(), 120 ),'-',''),' ',''),':','')\\\\nset @str='BACKUP LOG [' + @dbname + '] TO  DISK = N''E:/' + @dbname + '_' + @localtime + '_2log2_2reconvery2.bak'' WITH FORMAT, INIT'\\\\nexec(@str)\\\\ngo",
        "RequestId": "8d53700f-b80b-415a-8738-0c340eff2057"
    }
}
```

**Example 3: 查询创建全量备份+日志增量的命令**

在需要事务日志做增量导入时使用，此时获取的是不恢复的全量备份。
命令中\\\\n为换行符。

Input: 

```
tccli sqlserver DescribeBackupCommand --cli-unfold-argument  \
    --BackupFileType FULL_LOG \
    --DataBaseName db1 \
    --IsRecovery NO \
    --LocalPath E:/
```

Output: 
```
{
    "Response": {
        "Command": "declare @dbname varchar(100)\\\\ndeclare @localtime varchar(20)\\\\ndeclare @str varchar(8000)\\\\nset @dbname='db1'\\\\nset @localtime =replace(replace(replace(CONVERT(varchar, getdate(), 120 ),'-',''),' ',''),':','')\\\\nset @str='BACKUP DATABASE [' + @dbname + '] TO  DISK = N''E:/' + @dbname + '_' + @localtime + '_2full2_2noreconvery2.bak'' WITH INIT'\\\\nexec(@str)\\\\ngo",
        "RequestId": "03199d88-9dda-49eb-a045-7c69eb4d3591"
    }
}
```

