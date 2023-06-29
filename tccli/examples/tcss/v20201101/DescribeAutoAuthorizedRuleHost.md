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
                "Status": "xx",
                "PublicIp": "xx",
                "HostID": "xx",
                "MachineType": "xx",
                "DockerVersion": "xx",
                "InstanceID": "xx",
                "HostName": "xx",
                "ImageCnt": 1,
                "HostIP": "xx",
                "ContainerCnt": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

