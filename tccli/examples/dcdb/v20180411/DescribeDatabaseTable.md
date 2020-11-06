**Example 1: 查询数据库表中有哪些列**



Input: 

```
tccli dcdb DescribeDatabaseTable --cli-unfold-argument  \
    --InstanceId dcdbt-52s53yyh \
    --DbName test \
    --Table persons
```

Output: 
```
{
    "Response": {
        "RequestId": "6defc797-13eb-47ec-9a8f-dd3e407ff12c",
        "InstanceId": "dcdbt-52s53yyh",
        "DbName": "test",
        "Table": "persons",
        "Cols": [
            {
                "Col": "id",
                "Type": "bigint(20) unsigned"
            },
            {
                "Col": "name",
                "Type": "varchar(60)"
            },
            {
                "Col": "nick",
                "Type": "varchar(60)"
            }
        ]
    }
}
```

