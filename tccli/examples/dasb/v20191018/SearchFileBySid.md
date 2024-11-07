**Example 1: 搜索session列表**

搜索session列表

Input: 

```
tccli dasb SearchFileBySid --cli-unfold-argument  \
    --FileName 1.txt \
    --Offset 1 \
    --Sid dfac9070-8b23-499e-83b2-a50e3ca \
    --Limit 5 \
    --AuditLog True
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af",
        "SearchFileBySidResult": [
            {
                "Time": "2020-01-02T01:01:01+08:00",
                "Method": 1,
                "Protocol": "SFTP",
                "FileCurr": "/home/1.txt",
                "FileNew": "/home/2.txt",
                "Action": 1,
                "Size": 1024
            }
        ]
    }
}
```

