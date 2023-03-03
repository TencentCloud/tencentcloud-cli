**Example 1: 修改备份文件下载地址。**

通过该接口修改当前地域用户自定义的备份文件下载网络与地址。

Input: 

```
tccli redis ModifyBackupDownloadRestriction --cli-unfold-argument  \
    --LimitType Customize \
    --VpcComparisonSymbol In \
    --IpComparisonSymbol NotIn \
    --LimitVpc.0.VpcList vpc-5og4fwm9 vpc-03dsikyx \
    --LimitVpc.0.Region ap-guangzho \
    --LimitIp 10.1.0.13
```

Output: 
```
{
    "Response": {
        "RequestId": "489f7bc7-e0e0-4e6f-a5c4-97c5fcf7ea8b"
    }
}
```

