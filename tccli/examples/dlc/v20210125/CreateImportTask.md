**Example 1: 创建数据导入任务**



Input: 

```
tccli dlc CreateImportTask --cli-unfold-argument  \
    --InputType cos \
    --InputConf.0.Key fileType \
    --InputConf.0.Value CSV \
    --InputConf.1.Key sep \
    --InputConf.1.Value , \
    --InputConf.2.Key quote \
    --InputConf.2.Value " \
    --InputConf.3.Key header \
    --InputConf.3.Value true \
    --InputConf.4.Key paths \
    --InputConf.4.Value lakefs://@dlcda57--0205-4299-82a3/ \
    --OutputType lakefsStorage \
    --OutputConf.0.Key databaseName \
    --OutputConf.0.Value test_import \
    --OutputConf.1.Key tableName \
    --OutputConf.1.Value test_csv
```

Output: 
```
{
    "Response": {
        "TaskId": "xxxx-xxx",
        "RequestId": "123-abc"
    }
}
```

