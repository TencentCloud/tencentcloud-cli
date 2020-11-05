**Example 1: Modifying a data migration task**

This example shows you how to modify the configuration of migration task "dts-1kl0iy0v".

Input: 

```
tccli dts ModifyMigrateJob --cli-unfold-argument  \
    --JobId dts-1kl0iy0v\
    --JobName userdts\
    --DatabaseInfo [{"Database":"test","Table":["user","log"]}]\
    --MigrateOption.RunMode 1\
    --MigrateOption.MigrateType 2\
    --MigrateOption.MigrateObject 2\
    --MigrateOption.ConsistencyType 5\
    --MigrateOption.IsOverrideRoot 0\
    --DstInfo.ReadOnly 0\
    --SrcInfo.Supplier others
```

Output: 
```
{
    "Response": {
        "RequestId": "27ef2b7c-a786-48b4-9404-2f9baf3f4916"
    }
}
```

