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
                "Status": 1,
                "UpdateTime": "xx",
                "CertId": "xx",
                "ResourceType": "xx",
                "Region": "xx",
                "CreateTime": "xx",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

