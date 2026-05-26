**Example 1: 查询脱敏规则**



Input: 

```
tccli emr DescribeMaskRulesSTDV2 --cli-unfold-argument  \
    --InstanceId emr-ja22ar7t \
    --ServiceType HIVE
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DataMaskPolicyItems": [
                    {
                        "DataMaskInfo": {
                            "DataMaskType": "MASK_HASH",
                            "ValueExpr": ""
                        },
                        "Groups": [
                            "public"
                        ],
                        "Users": []
                    }
                ],
                "PolicyId": "88",
                "PolicyName": "hive-abaa2324-d962-4e6a-8d37-9ea5cdadf572",
                "Resource": {
                    "Catalog": "",
                    "Cell": "",
                    "Column": "id",
                    "ColumnFamily": "",
                    "ColumnQualifier": "",
                    "Database": "security_mask_test2",
                    "Namespace": "",
                    "Path": "",
                    "ResourceType": "column",
                    "Row": "",
                    "Schema": "",
                    "Table": "user_info",
                    "Topic": ""
                }
            }
        ],
        "TotalCount": 11,
        "RequestId": "212ccbaf-1af1-4bd4-b87a-cd75c045f426"
    }
}
```

