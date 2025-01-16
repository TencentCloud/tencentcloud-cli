**Example 1: CreateHiveTableByDDL**

创建表

Input: 

```
tccli wedata CreateHiveTableByDDL --cli-unfold-argument  \
    --DatasourceId 12342313 \
    --Database hive \
    --DDLSql Q1JFQVRFIFRBQkxFIGBhYWFgLmBiaWdfdGFibGVfMWAoCmBpZGAgaW50LApgbnVtMWAgaW50LApgbnVtMmAgaW50LApgbnVtM2AgaW50LApgbnVtNGAgaW50LApgbnVtNWAgaW50KQpyb3cgZm9ybWF0IGRlbGltaXRlZCAKZmllbGRzIHRlcm1pbmF0ZWQgYnkgJ1x0JyAKU1RPUkVEIEFTIFBBUlFVRVQ7 \
    --Incharge 231232 \
    --Privilege 0 \
    --ProjectId 124537 \
    --Type HIVE \
    --Async True
```

Output: 
```
{
    "Response": {
        "Data": "tablename",
        "TaskId": "25",
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

