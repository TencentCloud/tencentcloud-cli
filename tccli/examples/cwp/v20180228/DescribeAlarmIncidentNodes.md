**Example 1: 示例**

获取告警点所在事件的所有节点信息

Input: 

```
tccli cwp DescribeAlarmIncidentNodes --cli-unfold-argument  \
    --Uuid abc \
    --AlarmVid abc \
    --AlarmTime 0
```

Output: 
```
{
    "Response": {
        "IncidentNodes": [
            {
                "IncidentId": "abc",
                "TableName": "abc",
                "Vertex": [
                    {
                        "Type": 0,
                        "Vid": "abc",
                        "ParentVid": "abc",
                        "IsLeaf": true,
                        "ProcNamePrefix": "abc",
                        "ProcNameMd5": "abc",
                        "CmdLinePrefix": "abc",
                        "CmdLineMd5": "abc",
                        "FilePathPrefix": "abc",
                        "AddressPrefix": "abc",
                        "IsWeDetect": true,
                        "IsAlarm": true,
                        "FilePathMd5": "abc",
                        "AddressMd5": "abc"
                    }
                ],
                "VertexCount": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

