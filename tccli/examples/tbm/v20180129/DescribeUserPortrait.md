**Example 1: 查看品牌的用户画像结果**



Input: 

```
tccli tbm DescribeUserPortrait --cli-unfold-argument  \
    --BrandId qijGLCi6bE0weVWgO7fjvfo4Wvo9kfzujw%3D%3D
```

Output: 
```
{
    "Response": {
        "Age": {
            "PortraitSet": [
                {
                    "AgeRange": "0~18",
                    "Percent": 10.98
                },
                {
                    "AgeRange": "19~29",
                    "Percent": 50.77
                },
                {
                    "AgeRange": "30~39",
                    "Percent": 28.42
                },
                {
                    "AgeRange": "40~49",
                    "Percent": 7.1
                },
                {
                    "AgeRange": "50~69",
                    "Percent": 2.45
                },
                {
                    "AgeRange": "70+",
                    "Percent": 0.28
                }
            ]
        },
        "Gender": {
            "PortraitSet": [
                {
                    "Gender": "male",
                    "Percent": 60
                },
                {
                    "Gender": "female",
                    "Percent": 40
                }
            ]
        },
        "Province": {
            "PortraitSet": [
                {
                    "Percent": 0.93,
                    "Province": "天津"
                },
                {
                    "Percent": 1.6,
                    "Province": "山西"
                },
                {
                    "Percent": 12.86,
                    "Province": "福建"
                },
                {
                    "Percent": 1.47,
                    "Province": "甘肃"
                },
                {
                    "Percent": 0.17,
                    "Province": "青海"
                },
                {
                    "Percent": 3.75,
                    "Province": "北京"
                },
                {
                    "Percent": 3.08,
                    "Province": "浙江"
                },
                {
                    "Percent": 11.12,
                    "Province": "广东"
                },
                {
                    "Percent": 1.47,
                    "Province": "黑龙江"
                },
                {
                    "Percent": 8.44,
                    "Province": "四川"
                },
                {
                    "Percent": 2.14,
                    "Province": "安徽"
                },
                {
                    "Percent": 1.34,
                    "Province": "新疆"
                },
                {
                    "Percent": 5.09,
                    "Province": "河南"
                },
                {
                    "Percent": 2.68,
                    "Province": "上海"
                },
                {
                    "Percent": 2.81,
                    "Province": "湖南"
                },
                {
                    "Percent": 0.53,
                    "Province": "贵州"
                },
                {
                    "Percent": 0.13,
                    "Province": "澳门"
                },
                {
                    "Percent": 0.8,
                    "Province": "吉林"
                },
                {
                    "Percent": 0.53,
                    "Province": "宁夏"
                },
                {
                    "Percent": 2.68,
                    "Province": "陕西"
                },
                {
                    "Percent": 7.23,
                    "Province": "重庆"
                },
                {
                    "Percent": 1.6,
                    "Province": "江西"
                },
                {
                    "Percent": 0.26,
                    "Province": "台湾"
                },
                {
                    "Percent": 0.26,
                    "Province": "香港"
                },
                {
                    "Percent": 0.53,
                    "Province": "海南"
                },
                {
                    "Percent": 2.27,
                    "Province": "辽宁"
                },
                {
                    "Percent": 0.93,
                    "Province": "内蒙古"
                },
                {
                    "Percent": 3.61,
                    "Province": "河北"
                },
                {
                    "Percent": 0,
                    "Province": "西藏"
                },
                {
                    "Percent": 2.81,
                    "Province": "湖北"
                },
                {
                    "Percent": 6.97,
                    "Province": "山东"
                },
                {
                    "Percent": 6.56,
                    "Province": "江苏"
                },
                {
                    "Percent": 1.34,
                    "Province": "云南"
                },
                {
                    "Percent": 2.01,
                    "Province": "广西"
                }
            ]
        },
        "Movie": {
            "PortraitSet": [
                {
                    "Name": "最好的我们",
                    "Percent": 2.77
                },
                {
                    "Name": "快乐大本营",
                    "Percent": 2.42
                },
                {
                    "Name": "我的奇妙男友",
                    "Percent": 2.51
                }
            ]
        },
        "Star": {
            "PortraitSet": [
                {
                    "Name": "林正英",
                    "Percent": 2.77
                },
                {
                    "Name": "邓紫棋",
                    "Percent": 2.42
                },
                {
                    "Name": "成龙",
                    "Percent": 2.51
                }
            ]
        },
        "RequestId": "53240088-ccd6-4e4a-a7c5-c5a256806894"
    }
}
```

