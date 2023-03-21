**Example 1: 名片识别示例代码**



Input: 

```
tccli ocr BusinessCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "BusinessCardInfos": [
            {
                "Name": "姓名",
                "Value": "艾米",
                "ItemCoord": {
                    "X": 59,
                    "Y": 0,
                    "Width": 54,
                    "Height": 26
                }
            },
            {
                "Name": "职位",
                "Value": "视觉设计师",
                "ItemCoord": {
                    "X": 60,
                    "Y": 0,
                    "Width": 76,
                    "Height": 17
                }
            },
            {
                "Name": "部门",
                "Value": "社交平台部",
                "ItemCoord": {
                    "X": 60,
                    "Y": 0,
                    "Width": 76,
                    "Height": 15
                }
            },
            {
                "Name": "公司",
                "Value": "Tencent腾讯",
                "ItemCoord": {
                    "X": 61,
                    "Y": 0,
                    "Width": 164,
                    "Height": 26
                }
            },
            {
                "Name": "地址",
                "Value": "深圳市南山区高新技术园科技中一路腾讯大厦",
                "ItemCoord": {
                    "X": 59,
                    "Y": 0,
                    "Width": 321,
                    "Height": 17
                }
            },
            {
                "Name": "邮箱",
                "Value": "abcdefg@tencent.com",
                "ItemCoord": {
                    "X": 214,
                    "Y": 0,
                    "Width": 208,
                    "Height": 19
                }
            },
            {
                "Name": "手机",
                "Value": "+86-13312345678",
                "ItemCoord": {
                    "X": 100,
                    "Y": 0,
                    "Width": 165,
                    "Height": 18
                }
            },
            {
                "Name": "QQ",
                "Value": "1234567",
                "ItemCoord": {
                    "X": 78,
                    "Y": 0,
                    "Width": 89,
                    "Height": 17
                }
            },
            {
                "Name": "微信",
                "Value": "amy001",
                "ItemCoord": {
                    "X": 314,
                    "Y": 0,
                    "Width": 89,
                    "Height": 18
                }
            }
        ],
        "RetImageBase64": "",
        "Angle": 0,
        "RequestId": "98f8fcbf-933a-4e95-ac48-6f1a9308fs6h"
    }
}
```

