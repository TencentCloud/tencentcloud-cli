**Example 1: 获取反弹Shell列表**

获取反弹Shell列表

Input: 

```
tccli cwp DescribeReverseShellEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "UserName": "xx",
                "Status": 1,
                "ParentProcName": "xx",
                "DstIp": "xx",
                "Uuid": "xx",
                "CmdLine": "xx",
                "ProcTree": "xx",
                "MachineName": "xx",
                "DetectBy": 1,
                "ParentProcPath": "xx",
                "CreateTime": "xx",
                "ProcessName": "xx",
                "Hostip": "xx",
                "Quuid": "xx",
                "ParentProcGroup": "xx",
                "UserGroup": "xx",
                "FullPath": "xx",
                "DstPort": 1,
                "ParentProcUser": "xx",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

