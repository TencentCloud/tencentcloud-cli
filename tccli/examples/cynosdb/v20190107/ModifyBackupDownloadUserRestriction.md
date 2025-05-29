**Example 1: 修改用户当前地域的备份文件限制**



Input: 

```
tccli cynosdb ModifyBackupDownloadUserRestriction --cli-unfold-argument  \
    --LimitType NoLimit \
    --VpcComparisonSymbol  \
    --IpComparisonSymbol 
```

Output: 
```
{
    "Response": {
        "RequestId": "1530aee8-5130-45ce-9f4e-dfb50a55e4d4"
    }
}
```

