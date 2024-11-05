**Example 1: 查询内网间访问控制列表**

查询内网间访问控制列表，其中Filters中 IpVersion为0表示查询ipv4的规则列表

Input: 

```
tccli cfw DescribeVpcAcRule --cli-unfold-argument  \
    --Filters.0.Name IpVersion \
    --Filters.0.Values 0 \
    --Filters.0.OperatorType 1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "Uuid": 221579,
                "InternalUuid": 1729666998976364,
                "OrderIndex": 1,
                "SourceContent": "mb_1256532032_1666263807415",
                "SourceType": "template",
                "DestContent": "192.168.1.2",
                "DestType": "net",
                "Port": "-1/-1",
                "Protocol": "TCP",
                "RuleAction": "accept",
                "Description": "用于测试的规则",
                "Enable": "true",
                "Deleted": 0,
                "EdgeId": "ALL",
                "EdgeName": "edge名称",
                "DetectedTimes": 0,
                "FwGroupId": "ALL",
                "FwGroupName": "互联分组",
                "BetaList": [
                    {
                        "TaskId": "9001",
                        "TaskName": "autotest",
                        "LastTime": "1999-01-01 00:00:01"
                    }
                ],
                "ParamTemplateId": "pp-ie03er",
                "ParamTemplateName": "常规端口模版",
                "TargetName": "模版规则",
                "SourceName": "模版规则",
                "IpVersion": 0
            }
        ],
        "RequestId": "9afc19d7-0036-4f3d-af1a-80088236f4ed"
    }
}
```

**Example 2: 查询内网间访问控制列表示例2**

查询内网间访问控制列表，其中Filters中 IpVersion为0表示查询ipv4的规则列表，且基于源ip过滤

Input: 

```
tccli cfw DescribeVpcAcRule --cli-unfold-argument  \
    --Filters.0.Name SrcIP \
    --Filters.0.Values 192.168.1.10 \
    --Filters.0.OperatorType 9 \
    --Filters.1.Name IpVersion \
    --Filters.1.Values 0 \
    --Filters.1.OperatorType 1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "Uuid": 221579,
                "InternalUuid": 1729666998976364,
                "OrderIndex": 1,
                "SourceContent": "mb_1256532032_1666263807415",
                "SourceType": "template",
                "DestContent": "192.168.1.2",
                "DestType": "net",
                "Port": "-1/-1",
                "Protocol": "TCP",
                "RuleAction": "accept",
                "Description": "用于测试的规则",
                "Enable": "true",
                "Deleted": 0,
                "EdgeId": "ALL",
                "EdgeName": "edge名称",
                "DetectedTimes": 0,
                "FwGroupId": "ALL",
                "FwGroupName": "互联分组",
                "BetaList": [
                    {
                        "TaskId": "9001",
                        "TaskName": "autotest",
                        "LastTime": "1999-01-01 00:00:01"
                    }
                ],
                "ParamTemplateId": "pp-ie03er",
                "ParamTemplateName": "常规端口模版",
                "TargetName": "模版规则",
                "SourceName": "模版规则",
                "IpVersion": 0
            }
        ],
        "RequestId": "9afc19d7-0036-4f3d-af1a-80088236f4ed"
    }
}
```

