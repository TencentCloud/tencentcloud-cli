**Example 1: AddPartitions示例**



Input: 

```
tccli tccatalog AddPartitions --cli-unfold-argument  \
    --CatalogName layyu_lakehouse \
    --SchemaName s1 \
    --TableName t1 \
    --Partitions.0.Type IDENTITY \
    --Partitions.0.IdentityPartition.Name dt=20201014 \
    --Partitions.0.IdentityPartition.FieldNames dt \
    --Partitions.0.IdentityPartition.Values.0.Value 20201014 \
    --Partitions.0.IdentityPartition.Values.0.DataType string \
    --Partitions.0.IdentityPartition.Properties.0.Key k1 \
    --Partitions.0.IdentityPartition.Properties.0.Value v1
```

Output: 
```
{
    "Response": {
        "Partitions": [
            {
                "IdentityPartition": {
                    "FieldNames": [
                        "dt"
                    ],
                    "Name": "dt=20201014",
                    "Properties": [
                        {
                            "Key": "transient_lastDdlTime",
                            "Value": "1761110952"
                        }
                    ],
                    "Values": [
                        {
                            "DataType": "string",
                            "Value": "20201014"
                        }
                    ]
                },
                "Type": "identity"
            }
        ],
        "RequestId": "1f243c43-f973-4c97-8c5a-cf5940d8f718"
    }
}
```

