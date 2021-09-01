**Example 1: 查询识别结果**



Input: 

```
tccli gme DescribeFilterResult --cli-unfold-argument  \
    --BizId 0 \
    --FileId test_file_id
```

Output: 
```
{
    "Response": {
        "Data": {
            "BizId": 0,
            "Data": [
                {
                    "Type": 1,
                    "Word": "xxxx"
                }
            ],
            "FileId": "test_file_id",
            "FileName": "test_file_name",
            "OpenId": "",
            "Timestamp": "0000-00-00 00:00:00"
        },
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

