**Example 1: 查询当前地域用户设置的备份文件的下载来源限制。**

通过该接口查询当前地域用户设置的备份文件的下载来源限制。

Input: 

```
tccli redis DescribeBackupDownloadRestriction --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IpComparisonSymbol": "NotIn",
        "LimitIp": [
            "10.1.0.13"
        ],
        "LimitType": "Customize",
        "LimitVpc": [
            {
                "Region": "ap-guangzhou",
                "VpcList": [
                    "vpc-5og4fwm9",
                    "vpc-03dsikyx"
                ]
            }
        ],
        "RequestId": "785b6c5f-999f-43ef-9906-14f4c24b8040",
        "VpcComparisonSymbol": "In"
    }
}
```

