**Example 1: 创建cos备份**



Input: 

```
tccli bdrc CreateFileBackup --cli-unfold-argument  \
    --ResourceId brc-eva1-260095320 \
    --BackupStorageId vault-66sdscu3 \
    --BackupName test-acl \
    --ResourceType COS_AGENT \
    --EnableObjectAcl True \
    --EnableObjectTags True
```

Output: 
```
{
    "Response": {
        "BackupId": "cosbk-bgp33lr1",
        "RequestId": "3debff38-aeb0-436f-84be-14a445b1ed82"
    }
}
```

