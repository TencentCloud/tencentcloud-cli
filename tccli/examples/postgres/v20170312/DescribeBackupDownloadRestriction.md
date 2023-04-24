**Example 1: 查询备份文件下载限制**

 查询备份文件下载限制

Input: 

```
tccli postgres DescribeBackupDownloadRestriction --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RestrictionType": "Customize",
        "VpcRestrictionEffect": "Allow",
        "VpcIdSet": [
            "vpc-15ld6dhr"
        ],
        "IpRestrictionEffect": "",
        "IpSet": [],
        "RequestId": "be3bafde-f34e-4fda-9f40-04c5515e2148"
    }
}
```

