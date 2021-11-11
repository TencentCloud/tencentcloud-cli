**Example 1: 查询备份下载来源限制**



Input: 

```
tccli cdb DescribeBackupDownloadRestriction --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IpComparisonSymbol": "NotIn",
        "LimitIp": [
            "1.2.3.4",
            "192.168.10.0/24"
        ],
        "LimitType": "Customize",
        "LimitVpc": [
            {
                "Region": "ap-guangzhou",
                "VpcList": [
                    "vpc-aa3ximox",
                    "vpc-64elqxc9"
                ]
            }
        ],
        "RequestId": "b0439fbf-f835-4327-bed8-184d48ef43db",
        "VpcComparisonSymbol": "In"
    }
}
```

