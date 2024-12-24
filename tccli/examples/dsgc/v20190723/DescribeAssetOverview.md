**Example 1: 查询数据资产概览接口**

资产报告 - 查询数据资产概览接口

Input: 

```
tccli dsgc DescribeAssetOverview --cli-unfold-argument  \
    --DspaId dspa-44b7bd87 \
    --ComplianceId 1 \
    --AssetList.0.DataSourceType cdb \
    --AssetList.0.DataSourceInfo.0.DataSourceId cdb-14njkefc \
    --AssetList.0.DataSourceInfo.0.BindList test_db
```

Output: 
```
{
    "Response": {
        "DBInstanceNums": 0,
        "DBNums": 0,
        "TableNums": 0,
        "FieldNums": 0,
        "DBInstanceDistribution": [
            {
                "Key": "第一个数据源",
                "Value": 1
            }
        ],
        "DBDistribution": [
            {
                "Key": "第二个数据源",
                "Value": 2
            }
        ],
        "BucketNums": 0,
        "FileNums": 0,
        "Remark": "数据源cdb-23uhda9s未扫描",
        "EsInstanceNums": 1,
        "EsIndexNums": 1,
        "EsFieldNums": 1,
        "MongoInstanceNums": 1,
        "MongoDbNums": 1,
        "MongoColNums": 1,
        "MongoFieldNums": 1,
        "RequestId": "7020bf74-4fec-0aab-6a3c-52c2e94ad60a"
    }
}
```

