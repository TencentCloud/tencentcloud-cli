**Example 1: 示例**

示例

Input: 

```
tccli wedata CreateOnlineTable --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --ResourceGroupId res-02a91c5d \
    --TargetPath.CatalogName DataLakeCatalog \
    --TargetPath.SchemaName tiny_test \
    --TargetPath.TableName test_tiny_online \
    --ConnectionId a2b5af50-dd15-482e-9f28-ed95e64b2b13 \
    --OfflineFeatureConfiguration.TableNameInfo.CatalogName DataLakeCatalog \
    --OfflineFeatureConfiguration.TableNameInfo.SchemaName tiny_test \
    --OfflineFeatureConfiguration.TableNameInfo.TableName test_tiny \
    --OfflineFeatureConfiguration.PrimaryKeys tt \
    --OfflineFeatureConfiguration.TimestampColumn data \
    --TaskSchedulerConfiguration.Trigger.TriggerMode SNAPSHOT
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "53dd2043-8ad8-45ed-a334-4dcf3cdf0d9b"
    }
}
```

