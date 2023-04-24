**Example 1: 修改备份下载限制**

 修改备份下载限制

Input: 

```
tccli postgres ModifyBackupDownloadRestriction --cli-unfold-argument  \
    --RestrictionType CUSTOMIZE \
    --VpcRestrictionEffect ALLOW \
    --VpcIdSet vpc-15ld6dhr \
    --IpRestrictionEffect 
```

Output: 
```
{
    "Response": {
        "RequestId": "be3bafde-f34e-4fda-9f40-04c5515e2148"
    }
}
```

