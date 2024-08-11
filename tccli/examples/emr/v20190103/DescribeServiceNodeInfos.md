**Example 1: 查询服务进程信息**

查询服务进程信息

Input: 

```
tccli emr DescribeServiceNodeInfos --cli-unfold-argument  \
    --InstanceId emr-3qg9lptu \
    --ServiceGroupType 1 \
    --ServiceNodeType 1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCnt": 0,
        "ServiceNodeList": [
            {
                "Ip": "abc",
                "NodeType": 0,
                "NodeName": "abc",
                "ServiceStatus": 0,
                "MonitorStatus": 0,
                "Status": 0,
                "PortsInfo": "abc",
                "LastRestartTime": "abc",
                "Flag": 0,
                "ConfGroupId": 0,
                "ConfGroupName": "abc",
                "ConfStatus": 0,
                "ServiceDetectionInfo": [
                    {
                        "DetectAlert": "abc",
                        "DetetcFunctionKey": "abc",
                        "DetetcFunctionValue": "abc",
                        "DetetcTime": "abc",
                        "DetectFunctionKey": "abc",
                        "DetectFunctionValue": "abc",
                        "DetectTime": "abc"
                    }
                ],
                "NodeFlagFilter": "abc",
                "HealthStatus": {
                    "Code": 0,
                    "Text": "abc",
                    "Desc": "abc"
                },
                "IsSupportRoleMonitor": true,
                "StopPolicies": [
                    {
                        "Name": "abc",
                        "DisplayName": "abc",
                        "Describe": "abc",
                        "BatchSizeRange": [
                            0
                        ],
                        "IsDefault": "abc"
                    }
                ],
                "HAState": "abc",
                "NameService": "abc",
                "IsFederation": true
            }
        ],
        "AliasInfo": "abc",
        "SupportNodeFlagFilterList": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

