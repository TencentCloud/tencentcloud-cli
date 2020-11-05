**Example 1: Creating instance backups**



Input: 

```
tccli mongodb CreateBackupDBInstance --cli-unfold-argument  \
    --InstanceId cmgo-ayxpky6l\
    --BackupRemark remarkInfo\
    --BackupMethod 0
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": 4773,
        "RequestId": "e600a8d0-9014-11ea-84c1-01cccde830c6"
    }
}
```

