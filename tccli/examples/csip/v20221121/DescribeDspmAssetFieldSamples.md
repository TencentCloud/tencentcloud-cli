**Example 1: 查询dspm资产字段样本值**



Input: 

```
tccli csip DescribeDspmAssetFieldSamples --cli-unfold-argument  \
    --AssetId tdsql-5a07uua3 \
    --DbName dspm01 \
    --TableName encryption \
    --FieldName id \
    --MemberId mem-12e1e311 \
    --SchemaName schema
```

Output: 
```
{
    "Response": {
        "DataSet": [
            "1"
        ],
        "RequestId": "1d90b55c-ff1d-4683-a059-ec7f98c294da"
    }
}
```

