**Example 1: 查看操作系统支持的芯片列表**



Input: 

```
tccli iotvideo DescribeOsList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Android": [
                {
                    "ChipId": "AK3918EV300",
                    "ChipManufacture": "安凯（广州）微电子技术有限公司"
                }
            ],
            "Linux": [
                {
                    "ChipId": "AK3918EV300",
                    "ChipManufacture": "安凯（广州）微电子技术有限公司"
                },
                {
                    "ChipId": "FH8632",
                    "ChipManufacture": "上海富瀚微电子股份有限公司"
                },
                {
                    "ChipId": "FH8852",
                    "ChipManufacture": "上海富瀚微电子股份有限公司"
                }
            ],
            "LiteOs": [
                {
                    "ChipId": "Hi3518EV300",
                    "ChipManufacture": "深圳市海思半导体有限公司"
                },
                {
                    "ChipId": "Hi3516DV300",
                    "ChipManufacture": "深圳市海思半导体有限公司"
                }
            ]
        },
        "RequestId": "ae050c53-4009-43bc-9e02-5b7327bb719f"
    }
}
```

