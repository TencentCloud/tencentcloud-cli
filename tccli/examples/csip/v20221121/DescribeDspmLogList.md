**Example 1: 根据风险等级升序查询日志列表**

根据风险等级升序查询日志列表

Input: 

```
tccli csip DescribeDspmLogList --cli-unfold-argument  \
    --Sort desc \
    --DbPort 0 \
    --FuzzySearch select \
    --HitRule 0 \
    --DangerLevel high \
    --RestoreLogId 0 \
    --AssetsId 0 \
    --UserName root \
    --DbIp 127.0.0.1 \
    --Field ip \
    --SessionId 1711987200000-140227893131008-2045 \
    --Limit 1 \
    --StartTime 0 \
    --Offset 1 \
    --EndTime 0 \
    --ClientSideIp 127.0.0.1 \
    --DbName mysql \
    --ClientName Proxy
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "AiScore": 1,
                "AppUser": "testuser",
                "BackPacket": "",
                "ClientIp": "127.0.0.1",
                "ClientMac": "52:54:00:c9:38:87",
                "ClientName": "root",
                "ClientUser": "39510",
                "ClientPort": 3306,
                "DangerLevel": 1,
                "DbIp": "127.0.0.1",
                "DbName": "monitor",
                "DbPort": 3306,
                "DbUser": "root",
                "EffectRow": 0,
                "ExecTime": 1,
                "HitRule": "10000",
                "Id": 104709,
                "InstanceId": 1,
                "InstanceName": "审计测试资产",
                "OpSql": "login",
                "OpTime": 1631760308,
                "RetMsg": "login failed",
                "RetNo": 0,
                "SessionId": "1631721600000-140388847871744-5319",
                "SqlType": "LOGIN",
                "TableName": "information_schema",
                "AssetName": "审计测试资产",
                "HitRules": [],
                "SourceType": "cdb",
                "ReqId": "req-testidaseeada",
                "SqlMainType": "DML",
                "TableNames": [
                    "table1,table2,table3"
                ],
                "FieldNames": [
                    "field1,field2,field3"
                ],
                "FieldName": "phonenum,username,id",
                "DbType": "MYSQL",
                "ClientDriverName": "mongosh"
            }
        ],
        "RequestId": "a8aa8bbc-c255-42b1-88c4-04419f435a77"
    }
}
```

