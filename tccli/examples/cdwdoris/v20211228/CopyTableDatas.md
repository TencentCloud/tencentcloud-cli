**Example 1: 复制表**

复制SourceDb.SourceTable表到TargetDb.TargetTable

Input: 

```
tccli cdwdoris CopyTableDatas --cli-unfold-argument  \
    --InstanceId cdwdoris-bjizjxxx \
    --CopiedFromDb SourceDb \
    --CopiedFromTable SourceTable \
    --CopyToDb TargetDb \
    --CopyToTable TargetTable
```

Output: 
```
{
    "Response": {
        "Message": "",
        "RequestId": "894fc11c-393c-4ab7-bfac-ba64af52b1f9"
    }
}
```

