**Example 1: 查询证书云资源部署记录列表**

查询证书云资源部署记录列表

Input: 

```
tccli ssl DescribeHostDeployRecord --cli-unfold-argument  \
    --CertificateId vyRlKIeI
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DeployRecordList": [
            {
                "Id": 748932,
                "CertId": "vyRlKIeI",
                "ResourceType": "clb",
                "Region": "ap-guangzhou",
                "Status": 1,
                "CreateTime": "2023-09-19 12:00:00",
                "UpdateTime": "2023-09-19 13:00:00"
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

