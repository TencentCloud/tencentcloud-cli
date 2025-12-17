**Example 1: DescribeFunctions**



Input: 

```
tccli tccatalog DescribeFunctions --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName aorakili_test \
    --FunctionNames example_func2
```

Output: 
```
{
    "Response": {
        "Functions": [
            {
                "Audit": {
                    "CreatedAt": 1761717002179,
                    "CreatedTime": "2025-10-29 13:50:02",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": 1762410831490,
                    "LastModifiedTime": "2025-11-06 14:33:51",
                    "LastModifier": "1290245077@qq.com"
                },
                "ClassName": "com.example.udf.ToUpper",
                "EngineType": "spark",
                "FunctionType": "java",
                "Name": "example_func2",
                "Resources": [
                    {
                        "ResourceType": "jar",
                        "Uri": "hdfs:///user/spark/udfs/example-udf.jarexample-udf.jar"
                    }
                ]
            }
        ],
        "RequestId": "00c245e6-dc19-41bc-bfb0-fedaad4622b7"
    }
}
```

