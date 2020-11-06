**Example 1: 查询图片详情**

根据图片id查询图片详细信息

Input: 

```
tccli ape DescribeImage --cli-unfold-argument  \
    --ImageId 4723211
```

Output: 
```
{
    "Response": {
        "RequestId": "s1589767450135506558",
        "ImageId": 4723211,
        "Title": "优雅。黑色礼服的年轻时装模特",
        "Description": "",
        "PreviewUrl": "https://test.com/4723211.jpg",
        "ThumbUrl": "https://test.com/4723211.jpg",
        "Vendor": "xxx公司",
        "Marshals": [
            {
                "MarshalId": 4,
                "Height": 933,
                "Width": 1400,
                "Size": 0,
                "Format": "jpg",
                "Price": 1000,
                "LicenseScope": "标准授权",
                "IsVip": false
            },
            {
                "MarshalId": 5,
                "Height": 933,
                "Width": 1400,
                "Size": 0,
                "Format": "jpg",
                "Price": 0,
                "LicenseScope": "标准授权",
                "IsVip": true
            }
        ]
    }
}
```

