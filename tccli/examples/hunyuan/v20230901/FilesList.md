**Example 1: 文件列表。**

文件列表。

Input: 

```
tccli hunyuan FilesList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "c422c508-6d70-4529-83e0-d20ac5125852",
        "Total": 10,
        "Object": "list",
        "Data": [
            {
                "ID": "file-YbhlphnNEsjRoKTEXukAqNZZ",
                "Object": "file",
                "Bytes": 422915,
                "CreatedAt": 1722513746,
                "Filename": "云API产品简介.pdf",
                "Purpose": "file-extract"
            }
        ]
    }
}
```

