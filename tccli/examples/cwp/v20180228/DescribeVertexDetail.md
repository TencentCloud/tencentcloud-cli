**Example 1: 示例**

获取指定点属性信息

Input: 

```
tccli cwp DescribeVertexDetail --cli-unfold-argument  \
    --VertexIds dd8c40c6737f75a0c24244d6f4fa6173 \
    --IncidentId 468314cc-4004-492d-a974-7bf5666cb11b \
    --TableName incidents_dwewd
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
                "FileMd5": "472c65af3f43136472d1a383f5******",
                "FileContent": "njdskhsj",
                "FilePath": "/var/tmp",
                "FileCreateTime": "2020-11-21 15:16:00",
                "Address": "ad1",
                "DstPort": 18888,
                "SrcIP": "10.0.1.92",
                "User": "root",
                "VulName": "Apache ActiveMQ远程代码执行漏洞(CVE-2023-46604)",
                "VulTime": "2020-11-21 15:16:00",
                "HttpContent": "bodybody",
                "VulSrcIP": "10.0.1.92",
                "VertexId": "dd8c40c6737f75a0c24244d6f4fa6173"
            }
        ],
        "RequestId": "acdd5474-6360-4fd4-bfc7-843162cb8116"
    }
}
```

