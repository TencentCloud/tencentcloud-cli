**Example 1: 修改备份下载来源限制**



Input: 

```
tccli cdb ModifyBackupDownloadRestriction --cli-unfold-argument  \
    --LimitType Customize \
    --VpcComparisonSymbol In \
    --LimitVpc.0.Region ap-guangzhou \
    --LimitVpc.0.VpcList vpc-64elqxc9 vpc-aa3ximox \
    --IpComparisonSymbol NotIn \
    --LimitIp 192.168.10.0/24 1.2.3.4
```

Output: 
```
{
    "Response": {
        "RequestId": "7fd6ee14-ad09-4c58-9612-65d4d1691d50"
    }
}
```

