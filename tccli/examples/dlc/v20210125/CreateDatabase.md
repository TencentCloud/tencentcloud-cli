**Example 1: 生成建库SQL语句**



Input: 

```
tccli dlc CreateDatabase --cli-unfold-argument  \
    --DatabaseInfo.Comment create by nick \
    --DatabaseInfo.Properties.0.Value env \
    --DatabaseInfo.Properties.0.Key dev \
    --DatabaseInfo.DatabaseName testDB
```

Output: 
```
{
    "Response": {
        "Execution": {
            "SQL": "CREATE DATABASE IF NOT EXISTS `DataLakeCatalog`.`testDB` COMMENT 'create by nick' WITH DBPROPERTIES ('env'='dev')"
        },
        "RequestId": "2f67771a-a384-4b4e-86a5-146d8829ae2d"
    }
}
```

