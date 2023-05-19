**Example 1: 查询证书云资源更新记录列表**

查询证书云资源更新记录列表

Input: 

```
tccli ssl DescribeHostUpdateRecord --cli-unfold-argument  \
    --OldCertificateId zYrIXwpu
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DeployRecordList": [
            {
                "Id": 1,
                "CertId": "zXkBVP88",
                "OldCertId": "zYrIXwpu",
                "ResourceTypes": [
                    "cdn"
                ],
                "Status": 1,
                "CreateTime": "2022-10-09 17:38:38",
                "UpdateTime": "2022-10-09 19:21:35"
            }
        ],
        "RequestId": "1111111111111"
    }
}
```

