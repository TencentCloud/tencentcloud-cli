**Example 1: 查询证书ddos云资源部署实例列表**

查询证书ddos云资源部署实例列表

Input: 

```
tccli ssl DescribeHostDdosInstanceList --cli-unfold-argument  \
    --ResourceType ddos \
    --IsCache 1 \
    --CertificateId abc \
    --Filters.0.FilterKey abc \
    --Filters.0.FilterValue abc
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "abc",
                "InstanceId": "abc",
                "Protocol": "abc",
                "CertId": "abc",
                "VirtualPort": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

