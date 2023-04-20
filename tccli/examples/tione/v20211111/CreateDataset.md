**Example 1: 创建数据集**

CreateDataset

Input: 

```
tccli tione CreateDataset --cli-unfold-argument  \
    --DatasetName test \
    --AnnotationStatus STATUS_NON_ANNOTATED \
    --SchemaInfos.0.Type  \
    --SchemaInfos.0.Name  \
    --StorageDataPath.Paths input/ \
    --StorageDataPath.Region ap-guangzhou \
    --StorageDataPath.Bucket test-1256580188 \
    --StorageLabelPath.Paths output/ \
    --StorageLabelPath.Region ap-guangzhou \
    --StorageLabelPath.Bucket test-1256580188 \
    --DatasetType TYPE_DATASET_TEXT \
    --IsSchemaExisted False \
    --ContentType TYPE_TEXT_LINE
```

Output: 
```
{
    "Response": {
        "DatasetId": "ds-4575dwt7",
        "RequestId": "3d033484-30f4-42e7-837e-825f33fdd23b"
    }
}
```

