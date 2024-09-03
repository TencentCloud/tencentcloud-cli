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
                "Id": 1,
                "CertId": "abc",
                "ResourceType": "abc",
                "Region": "abc",
                "Status": 1,
                "CreateTime": "abc",
                "UpdateTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

