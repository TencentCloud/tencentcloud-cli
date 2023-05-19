**Example 1: 获取主机安全服务列表**

获取主机安全服务列表

Input: 

```
tccli ssl DescribeHostWafInstanceList --cli-unfold-argument  \
    --CertificateId abc \
    --IsCache 1 \
    --Filters.0.FilterKey abc \
    --Filters.0.FilterValue abc \
    --ResourceType abc \
    --OldCertificateId abc
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "abc",
                "CertId": "abc",
                "Status": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

