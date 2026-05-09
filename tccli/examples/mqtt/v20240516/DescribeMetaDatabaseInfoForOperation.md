**Example 1: 示例**



Input: 

```
tccli mqtt DescribeMetaDatabaseInfoForOperation --cli-unfold-argument  \
    --CdbId cdb-3x542xo
```

Output: 
```
{
    "Response": {
        "CdbId": "cdb-3x542xo",
        "CdbName": "cde-test",
        "CreateTime": 1777452688000,
        "JdbcUrl": "jdbc:mysql://*********:3306/mqtt_meta?useUnicode=true&characterEncoding=utf-8&zeroDateTimeBehavior=convertToNull&serverTimezone=GMT%2B8&socketTimeout=60000&connectTimeout=3000",
        "ParamOne": "r**t",
        "ParamTwo": "**",
        "UpdateTime": 1777452688000,
        "RequestId": "bc8c88d8-3735-43a7-aef8-929dc3f1b1b6"
    }
}
```

