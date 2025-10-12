**Example 1: 查询数据源**



Input: 

```
tccli wedata GetDataSource --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --Id 62268
```

Output: 
```
{
    "Response": {
        "Data": {
            "Category": "DB",
            "CreateTime": "2025-09-03 00:11:03",
            "CreateUser": "100028579606",
            "Description": null,
            "DevConProperties": null,
            "DisplayName": "mysql_2",
            "Id": 62268,
            "ModifyTime": "2025-09-03 00:11:03",
            "ModifyUser": "100028579606",
            "Name": "mysql_2",
            "ProdConProperties": "{\"newType\":1,\"connectType\":\"public\",\"ip\":\"1.1.1.1\",\"type\":\"MYSQL\",\"authorityType\":\"true\",\"deployType\":\"CONNSTR_CVMDB\",\"url\":\"jdbc:mysql://1.1.1.1:1111/database\",\"password\":\"********\",\"vpcTenantId\":\"1315051789\",\"port\":\"1111\",\"regionAbbr\":\"gz\",\"vpcId\":\"vpc-ds5rpnxh\",\"passwordEncrypt\":\"e3e5315db835fc7f7c70896fa3553d81\",\"region\":\"ap-guangzhou\",\"db\":\"database\",\"username\":\"aaaa\"}",
            "ProjectId": "1460947878944567296",
            "ProjectName": "[us_dev]",
            "Type": "MYSQL"
        },
        "RequestId": "6a721ba0-5459-4e10-b29f-4d43665b7024"
    }
}
```

