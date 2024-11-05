**Example 1: 查询自动授权规则授权范围主机信息**



Input: 

```
tccli tcss DescribeAutoAuthorizedRuleHost --cli-unfold-argument  \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "ContainerCnt": 2,
                "DockerVersion": "19.03.9",
                "HostID": "8bc803fd-d85d-47b8-9e2b-9644674be677",
                "HostIP": "1.1.1.1",
                "HostName": "机器名称",
                "ImageCnt": 1,
                "InstanceID": "ins-8bc803fd",
                "MachineType": "CVM",
                "PublicIp": "1.1.1.1",
                "Status": "ONLINE"
            }
        ],
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

