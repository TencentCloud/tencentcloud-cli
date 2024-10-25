**Example 1: 示例**

获取告警点所在事件的所有节点信息

Input: 

```
tccli cwp DescribeAlarmIncidentNodes --cli-unfold-argument  \
    --Uuid 1c26308c-5493-4eaf-a817-112ec25f499e \
    --AlarmVid 23eeeb4347bdd26bfc6b7ee9a3b755dd \
    --AlarmTime 0
```

Output: 
```
{
    "Response": {
        "IncidentNodes": [
            {
                "IncidentId": "xxxx-xx-xx-xxxx",
                "TableName": "events_bash",
                "Vertex": [
                    {
                        "Type": 0,
                        "Vid": "23eeeb4347bdd26bfc6b7ee9a3b755dd",
                        "ParentVid": "23eeeb4347bdd26bfc6b7ee9a3b755dd",
                        "IsLeaf": true,
                        "ProcNamePrefix": "python",
                        "ProcNameMd5": "23eeeb4347bdd26bfc6b7ee9a3b755dd",
                        "CmdLinePrefix": "python",
                        "CmdLineMd5": "23eeeb4347bdd26bfc6b7ee9a3b755dd",
                        "FilePathPrefix": "/root",
                        "AddressPrefix": "/root",
                        "IsWeDetect": true,
                        "IsAlarm": true,
                        "FilePathMd5": "887904812217cca9bc2b9adb875daf42",
                        "AddressMd5": "887904812217cca9bc2b9adb875daf42"
                    }
                ],
                "VertexCount": 0
            }
        ],
        "RequestId": "xxxxxxxx-1234-5678-9101-yyyyyyyyyy"
    }
}
```

