**Example 1: 查询安全组绑定的es集群列表信息**

查询安全组绑定的es集群列表信息

Input: 

```
tccli es DescribeSecurityGroupBindEs --cli-unfold-argument  \
    --SecurityGroupId sg-3p7lkvxx
```

Output: 
```
{
    "Response": {
        "SecurityGroupId": "sg-3p7lkvxx",
        "RequestId": "1",
        "EsBindSecurityGroupInfos": [
            {
                "InstanceId": "es-xxx1",
                "InstanceName": "es集群1",
                "VpcId": "vpc-xx1",
                "EsVip": "10.x.x.1",
                "EsPort": 9200
            },
            {
                "InstanceId": "es-xxx2",
                "InstanceName": "es集群2",
                "VpcId": "vpc-xx2",
                "EsVip": "10.x.x.2",
                "EsPort": 9200
            }
        ]
    }
}
```

