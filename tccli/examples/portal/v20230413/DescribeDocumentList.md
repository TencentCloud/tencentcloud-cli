**Example 1: 获取文档列表**

获取文档列表

Input: 

```
tccli portal DescribeDocumentList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CategoryId": 2436,
                "CategoryName": "test",
                "Disable": 0,
                "FirstReleaseTime": "0001-01-01T00:00:00Z",
                "Html": "",
                "Id": 81880,
                "Markdown": "",
                "RecentReleaseTime": "0001-01-01T00:00:00Z",
                "Title": "test"
            }
        ],
        "RequestId": "887cf563-a330-4a67-90e1-9dc343a6a7b1",
        "Total": 63999
    }
}
```

