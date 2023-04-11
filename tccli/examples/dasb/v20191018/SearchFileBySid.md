**Example 1: 搜索session列表**

搜索session列表

Input: 

```
tccli dasb SearchFileBySid --cli-unfold-argument  \
    --FileName 1.txt \
    --Offset 1 \
    --Sid xx \
    --Limit 5 \
    --AuditLog True
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "RequestId": "xx",
        "SearchFileBySidResult": [
            {
                "Time": "2020-01-02T01:01:01Z",
                "Method": 1,
                "Protocol": "SFTP",
                "FileCurr": "/home/1.txt",
                "FileNew": "/home/2.txt"
            }
        ]
    }
}
```

