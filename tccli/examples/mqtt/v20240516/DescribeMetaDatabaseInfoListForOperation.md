**Example 1: 示例**



Input: 

```
tccli mqtt DescribeMetaDatabaseInfoListForOperation --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CdbId": "cdb-1234",
                "CdbName": "mqtt-dev-cdb",
                "CreateTime": 1768295273000,
                "JdbcUrl": "jdbc:mysql://*************:3306/mqtt_meta_dev?useUnicode=true&characterEncoding=utf-8&zeroDateTimeBehavior=convertToNull&serverTimezone=GMT%2B8&socketTimeout=60000&connectTimeout=3000",
                "ParamOne": "root",
                "ParamTwo": "*************",
                "UpdateTime": 1768295273000
            }
        ],
        "RequestId": "c032fdf2-0af6-426c-9f78-030321df56a5"
    }
}
```

