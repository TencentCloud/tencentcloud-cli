**Example 1: 示例**

获取指定点属性信息

Input: 

```
tccli cwp DescribeVertexDetail --cli-unfold-argument  \
    --VertexIds abc \
    --IncidentId abc \
    --TableName abc
```

Output: 
```
{
    "Response": {
        "VertexDetails": [
            {
                "Type": 0,
                "Time": "abc",
                "AlarmInfo": [
                    {
                        "AlarmId": "abc",
                        "Status": 0
                    }
                ],
                "ProcName": "abc",
                "CmdLine": "abc",
                "Pid": "abc",
                "FileMd5": "abc",
                "FileContent": "abc",
                "FilePath": "abc",
                "FileCreateTime": "abc",
                "Address": "abc",
                "DstPort": 1,
                "SrcIP": "abc",
                "User": "abc",
                "VulName": "abc",
                "VulTime": "abc",
                "HttpContent": "abc",
                "VulSrcIP": "abc",
                "VertexId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

