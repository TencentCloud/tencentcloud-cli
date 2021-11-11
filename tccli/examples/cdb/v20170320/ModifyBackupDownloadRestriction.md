**Example 1: 修改备份下载来源限制**



Input: 

```
tccli cdb ModifyBackupDownloadRestriction --cli-unfold-argument  \
    --LimitType Customize \
    --VpcComparisonSymbol In \
    --IpComparisonSymbol NotIn \
    --LimitIp 1.2.3.4 192.168.10.0/24 \
    --LimitVpc.0.Region ap-guangzhou \
    --LimitVpc.0.VpcList vpc-aa3ximox vpc-64elqxc9
```

Output: 
```
{
    "Response": {
        "RequestId": "7fd6ee14-ad09-4c58-9612-65d4d1691d50"
    }
}
```

