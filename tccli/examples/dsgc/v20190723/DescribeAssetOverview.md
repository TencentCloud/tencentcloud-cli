**Example 1: 查询数据资产概览接口**

资产报告 - 查询数据资产概览接口

Input: 

```
tccli dsgc DescribeAssetOverview --cli-unfold-argument  \
    --DspaId abc \
    --ComplianceId 0 \
    --AssetList.0.DataSourceType abc \
    --AssetList.0.DataSourceInfo.0.DataSourceId abc \
    --AssetList.0.DataSourceInfo.0.BindList abc
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
                "Key": "abc",
                "Value": 0
            }
        ],
        "DBDistribution": [
            {
                "Key": "abc",
                "Value": 0
            }
        ],
        "BucketNums": 0,
        "FileNums": 0,
        "Remark": "abc",
        "EsInstanceNums": 1,
        "EsIndexNums": 1,
        "EsFieldNums": 1,
        "MongoInstanceNums": 1,
        "MongoDbNums": 1,
        "MongoColNums": 1,
        "MongoFieldNums": 1,
        "RequestId": "abc"
    }
}
```

