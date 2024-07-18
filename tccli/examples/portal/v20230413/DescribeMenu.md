**Example 1: 示例一**

查询Menu

Input: 

```
tccli portal DescribeMenu --cli-unfold-argument  \
    --ProductCode 1 \
    --Title abc \
    --DocumentLanguage abc
```

Output: 
```
{
    "Response": {
        "Children": [
            {
                "Children": [],
                "DocType": "default",
                "Id": 67350,
                "PdfUrl": "",
                "Pid": 66380,
                "PreviewUrl": "https://cloud.tencent.com/document/product/598/67350",
                "Source": "cam",
                "Title": "概览",
                "Type": "page"
            }
        ],
        "DocType": "default",
        "Id": 66380,
        "PdfUrl": "",
        "Pid": 0,
        "PreviewUrl": "https://cloud.tencent.com/document/product/598/66380",
        "Source": "cam",
        "Title": "支持CAM的业务接口",
        "Type": "directory",
        "RequestId": "cf8fbfe1-a070-43f7-abf3-0cb7cc0f3dd0"
    }
}
```

