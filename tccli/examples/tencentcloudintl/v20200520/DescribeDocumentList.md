**Example 1: 获取文档列表**

获取文档列表

Input: 

```
tccli tencentcloudintl DescribeDocumentList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Id 54220
```

Output: 
```
{
    "Response": {
        "RequestId": "12de358a-6689-4729-a636-479747e36f30",
        "Response": {
            "List": [
                {
                    "CategoryId": 1165,
                    "CategoryName": "模拟实时音视频",
                    "CategorySwitch": 0,
                    "Description": "",
                    "Disable": 0,
                    "DisableUpdateTime": "2024-12-03 19:07:30",
                    "DocumentLanguage": "en",
                    "Extension": "",
                    "FirstReleaseTime": "2024-12-03 11:07:30",
                    "Html": "",
                    "Id": 54220,
                    "InMenu": 1,
                    "Keyword": "",
                    "Markdown": "",
                    "RecentReleaseTime": "2024-12-03 11:07:30",
                    "RedirectUrl": "",
                    "ShowToc": 0,
                    "Slate": "",
                    "SlateSdkVersion": "",
                    "Source": "twrite",
                    "Title": "andrekzhu",
                    "Toc": "",
                    "Visible": 0,
                    "VisibleUpdateTime": "2024-12-03 19:07:30"
                }
            ],
            "RequestId": "12de358a-6689-4729-a636-479747e36f30",
            "Total": 1
        }
    }
}
```

