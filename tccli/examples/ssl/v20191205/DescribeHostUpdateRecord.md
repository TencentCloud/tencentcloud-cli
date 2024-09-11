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
                "CertId": "abc",
                "OldCertId": "abc",
                "ResourceTypes": [
                    "abc"
                ],
                "Regions": [
                    "abc"
                ],
                "Status": 1,
                "CreateTime": "abc",
                "UpdateTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

