**Example 1: test**

test

Input: 

```
tccli dlc GetOptimizerPolicy --cli-unfold-argument  \
    --SmartPolicy.BaseInfo.Uin 1000******03 \
    --SmartPolicy.BaseInfo.PolicyType Table \
    --SmartPolicy.BaseInfo.Catalog DataLakeCatalog \
    --SmartPolicy.BaseInfo.Database dlc_db \
    --SmartPolicy.BaseInfo.Table table_ai \
    --SmartPolicy.BaseInfo.AppId 131****789 \
    --SmartPolicy.Policy.Inherit none \
    --SmartPolicy.Policy.Resources.0.AttributionType group \
    --SmartPolicy.Policy.Resources.0.ResourceType SQL \
    --SmartPolicy.Policy.Resources.0.Name dlc_spark_test \
    --SmartPolicy.Policy.Resources.0.Instance spark-sql \
    --SmartPolicy.Policy.Resources.0.Favor.0.Priority 2147483647 \
    --SmartPolicy.Policy.Resources.0.Favor.0.Catalog DataLakeCatalog \
    --SmartPolicy.Policy.Resources.0.Favor.0.DataBase dlc_db \
    --SmartPolicy.Policy.Resources.0.Favor.0.Table table_ai \
    --SmartPolicy.Policy.Resources.0.Status 1 \
    --SmartPolicy.Policy.Resources.0.ResourceGroupName default-rg-1234dlc123 \
    --SmartPolicy.Policy.Written.WrittenEnable enable \
    --SmartPolicy.Policy.Lifecycle.LifecycleEnable disable \
    --SmartPolicy.Policy.Lifecycle.Expiration 0 \
    --SmartPolicy.Policy.Lifecycle.DropTable True \
    --SmartPolicy.Policy.Lifecycle.ExpiredField pt \
    --SmartPolicy.Policy.Lifecycle.ExpiredFieldFormat yyyy-MM-dd \
    --SmartPolicy.Policy.Index.IndexEnable disable \
    --SmartPolicy.Policy.ChangeTable.DataRetentionTime 8
```

Output: 
```
{
    "Response": {
        "RequestId": "43252d22-6ddf-4bda-81b5-575edf0f787c",
        "SmartOptimizerPolicy": {
            "Index": {
                "IndexEnable": "disable"
            },
            "Inherit": "none",
            "Lifecycle": {
                "LifecycleEnable": "disable"
            },
            "Resources": [
                {
                    "AttributionType": "group",
                    "Name": "dlc_spark_test",
                    "ResourceGroupName": "default-rg-1234dlc123",
                    "ResourceType": "SQL"
                }
            ],
            "Written": {
                "WrittenEnable": "enable"
            }
        }
    }
}
```

