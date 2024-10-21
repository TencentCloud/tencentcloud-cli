**Example 1: 示例**

获取指定点属性信息

Input: 

```
tccli cwp DescribeVertexDetail --cli-unfold-argument  \
    --VertexIds dd8c40c6737f75a0c24244d6f4fa6173 \
    --IncidentId 468314cc-4004-492d-a974-7bf5666cb11b \
    --TableName incidents_xxx
```

Output: 
```
{
    "Response": {
        "VertexDetails": [
            {
                "Type": 0,
                "Time": " 2019-12-25 11:57:15",
                "AlarmInfo": [
                    {
                        "AlarmId": "dd8c40c6",
                        "Status": 0
                    }
                ],
                "ProcName": "curl",
                "CmdLine": "curl",
                "Pid": "2534",
                "FileMd5": "",
                "FileContent": "",
                "FilePath": "",
                "FileCreateTime": "",
                "Address": "",
                "DstPort": 18888,
                "SrcIP": "",
                "User": "",
                "VulName": "",
                "VulTime": "",
                "HttpContent": "",
                "VulSrcIP": "",
                "VertexId": "dd8c40c6737f75a0c24244d6f4fa6173"
            }
        ],
        "RequestId": "xxxxxxxx-1234-5678-9101-yyyyyyyyyy"
    }
}
```

