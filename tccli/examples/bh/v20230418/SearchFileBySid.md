**Example 1: 搜索session列表**

搜索session列表

Input: 

```
tccli bh SearchFileBySid --cli-unfold-argument  \
    --FileName 1.txt \
    --Offset 1 \
    --Sid bh-test-sid-1a2b3c \
    --Limit 5 \
    --AuditLog True
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "RequestId": "b8ebf0b3-ecf5-49bf-9f9d-86341c4072f1",
        "SearchFileBySidResult": [
            {
                "Time": "2020-01-02T01:01:01Z",
                "Method": 1,
                "Size": 100,
                "Action": 1,
                "Protocol": "SFTP",
                "FileCurr": "/home/1.txt",
                "FileNew": "/home/2.txt"
            }
        ]
    }
}
```

