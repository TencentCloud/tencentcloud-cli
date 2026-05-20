**Example 1: 创建只读分析引擎实例**

本接口（AddLibraDBInstances）用于集群添加只读分析引擎

Input: 

```
tccli cynosdb AddLibraDBInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-7 \
    --ClusterId cynosdbmysql-037c8yll \
    --Cpu 4 \
    --Mem 16 \
    --StorageSize 100 \
    --PayMode 0 \
    --Objects.DatabaseTables.MigrateDBMode all \
    --GoodsNum 1 \
    --VpcId vpc-nnakli31 \
    --SubnetId subnet-558rhwt2
```

Output: 
```
{
    "Response": {
        "BigDealIds": null,
        "DealNames": [
            "20250417625002746837731"
        ],
        "RequestId": "173601bd-d6ab-4774-8714-775b37c8613d",
        "ResourceIds": [
            "libradb-ins-7ohnx2nu"
        ],
        "TranId": "20250417625002746837741"
    }
}
```

