**Example 1: 企业证照识别示例代码**

企业证照识别示例代码

Input: 

```
tccli ocr EnterpriseLicenseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "EnterpriseLicenseInfos": [
            {
                "Name": "统一社会信用代码",
                "Value": "91440300000XX0000H"
            },
            {
                "Name": "法定代表人",
                "Value": "李峰"
            },
            {
                "Name": "名称",
                "Value": "深圳市信息技术服务有限公司"
            },
            {
                "Name": "住所",
                "Value": "深圳市福田区沙头街道xxx街7号"
            },
            {
                "Name": "主体类型",
                "Value": "有限责任公司(自然人独资)"
            },
            {
                "Name": "成立日期",
                "Value": "2017年06月30日"
            }
        ],
        "Angle": 0,
        "RequestId": "f5b9110f-82db-4a5f-b872-ad39aa2eb09a"
    }
}
```

