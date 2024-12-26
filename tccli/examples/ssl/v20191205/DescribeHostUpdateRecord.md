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
                "Id": 73839,
                "CertId": "jdjenhss",
                "OldCertId": "zYrIXwpu",
                "ResourceTypes": [
                    "clb"
                ],
                "Regions": [
                    "ap-guangzhou"
                ],
                "Status": 1,
                "CreateTime": "2023-12-18 12:00:00",
                "UpdateTime": "2023-12-18 12:11:00"
            }
        ],
        "RequestId": "d9aa752b-dbd8-49c9-958f-75c051eddfe2"
    }
}
```

