**Example 1: 获取试卷切题任务**



Input: 

```
tccli ocr DescribeQuestionSplitJob --cli-unfold-argument  \
    --JobId 1486557414219153408
```

Output: 
```
{
    "Response": {
        "ErrorCode": "****",
        "ErrorMessage": "**",
        "JobStatus": "DONE",
        "QuestionInfo": [
            {
                "Angle": 0,
                "Height": 1232,
                "OrgHeight": 1232,
                "OrgWidth": 1600,
                "ResultList": [
                    {
                        "Answer": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 489,
                                        "Y": 252
                                    },
                                    "LeftTop": {
                                        "X": 489,
                                        "Y": 230
                                    },
                                    "RightBottom": {
                                        "X": 521,
                                        "Y": 252
                                    },
                                    "RightTop": {
                                        "X": 521,
                                        "Y": 230
                                    }
                                },
                                "GroupType": "",
                                "Index": 0,
                                "PageIndex": 1,
                                "Text": ""
                            }
                        ],
                        "Coord": [
                            {
                                "LeftBottom": {
                                    "X": 69,
                                    "Y": 381
                                },
                                "LeftTop": {
                                    "X": 69,
                                    "Y": 198
                                },
                                "RightBottom": {
                                    "X": 550,
                                    "Y": 381
                                },
                                "RightTop": {
                                    "X": 550,
                                    "Y": 198
                                }
                            }
                        ],
                        "Figure": [],
                        "Option": [],
                        "Parse": [],
                        "Question": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 69,
                                        "Y": 381
                                    },
                                    "LeftTop": {
                                        "X": 69,
                                        "Y": 198
                                    },
                                    "RightBottom": {
                                        "X": 550,
                                        "Y": 381
                                    },
                                    "RightTop": {
                                        "X": 550,
                                        "Y": 198
                                    }
                                },
                                "GroupType": "",
                                "Index": 0,
                                "PageIndex": 1,
                                "Text": "下列加点字的注音和字形全都正确的一项是(3 分)（）\\nA. $\\underset{\\cdot}{兴}$味(xīng) 俯$\\underset{\\cdot}{瞰}$(kàn) 鲜$\\underset{\\cdot}{腴}$(yú) 春寒料$\\underset{\\cdot}{俏}$(qiào)\\nB. $\\underset{\\cdot}{颓}$唐(tuí) 弧$\\underset{\\cdot}{形}$(hū) $\\underset{\\cdot}{消}$毁(xiāo) 摩肩接$\\underset{\\cdot}{踵}$(zhǒng)\\nC. $\\underset{\\cdot}{辟}$邪(bì) 依$\\underset{\\cdot}{傍}$(bàng) $\\underset{\\cdot}{蹒}$跚(pán) 因地$\\underset{\\cdot}{制}$宜(zhì)\\nD. 记$\\underset{\\cdot}{载}$(zài) 斟$\\underset{\\cdot}{酌}$(zhuó) $\\underset{\\cdot}{濒}$临(pín) 巧妙绝$\\underset{\\cdot}{轮}$(lún)"
                            }
                        ],
                        "Table": []
                    }
                ],
                "Width": 1600
            }
        ],
        "RequestId": "82db9eaf-875d-4b4d-a277-64cb002a0783"
    }
}
```

