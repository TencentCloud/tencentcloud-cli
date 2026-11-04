**Example 1: QueryType=0全文识别**

识别且输出全文内容

Input: 

```
tccli ocr RecognizeAgent --cli-unfold-argument  \
    --QueryType 0 \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/GeneralAccurateOCR/GeneralAccurateOCR1.jpg \
    --SelectModel 0
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "RequestId": "4cfcc12b-4626-4c59-b586-69c5420a038b",
        "Response": [
            {
                "Answer": "",
                "QueryInfo": "",
                "TextDetections": [
                    {
                        "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}",
                        "Confidence": 99,
                        "DetectedText": "学",
                        "ItemPolygon": {
                            "Height": 48,
                            "Width": 43,
                            "X": 563,
                            "Y": 41
                        },
                        "Polygon": [
                            {
                                "X": 563,
                                "Y": 44
                            },
                            {
                                "X": 602,
                                "Y": 41
                            },
                            {
                                "X": 606,
                                "Y": 85
                            },
                            {
                                "X": 567,
                                "Y": 89
                            }
                        ],
                        "WordCoordPoint": [],
                        "Words": []
                    },
                    {
                        "AdvancedInfo": "{\"Parag\":{\"ParagNo\":97}}",
                        "Confidence": 99,
                        "DetectedText": "获取证书",
                        "ItemPolygon": {
                            "Height": 179,
                            "Width": 44,
                            "X": 184,
                            "Y": 1334
                        },
                        "Polygon": [
                            {
                                "X": 190,
                                "Y": 1334
                            },
                            {
                                "X": 228,
                                "Y": 1335
                            },
                            {
                                "X": 222,
                                "Y": 1513
                            },
                            {
                                "X": 184,
                                "Y": 1511
                            }
                        ],
                        "WordCoordPoint": [],
                        "Words": []
                    }
                ]
            }
        ]
    }
}
```

**Example 2: QueryType=1判断**

判断输入图是否为{增值税发票}

Input: 

```
tccli ocr RecognizeAgent --cli-unfold-argument  \
    --Query 增值税专用发票 \
    --QueryType 1 \
    --ImageUrl https://example.com/judge-image.jpg \
    --SelectModel 0
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "Response": [
            {
                "Answer": "否",
                "QueryInfo": "根据图片内容，判断这张图是不是增值税专用发票？只回答 是 / 否"
            }
        ],
        "RequestId": "8c23f191-5bc6-43f5-9890-21f88e545f6c"
    }
}
```

**Example 3: QueryType=2分类**

自动分类输入图属于哪种发票类型

Input: 

```
tccli ocr RecognizeAgent --cli-unfold-argument  \
    --Query 增值税专用发票 增值税普通发票 通行费发票 \
    --QueryType 2 \
    --ImageUrl https://demo.com/invoice.jpg \
    --SelectModel 0
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "Response": [
            {
                "Answer": "增值税普通发票",
                "QueryInfo": "根据图片内容，该图片最符合以下哪种分类：增值税专用发票；增值税普通发票；通行费发票。只回答 增值税专用发票 / 增值税普通发票 / 通行费发票 ，若均不属于以上所有分类，只输出：均不符合。"
            }
        ],
        "RequestId": "6ed1170d-3eb2-42e4-a052-fd9bf1490402"
    }
}
```

**Example 4: QueryType=3总结提炼**

总结提炼简历图中与{课程}相关内容

Input: 

```
tccli ocr RecognizeAgent --cli-unfold-argument  \
    --Query 课程 \
    --QueryType 3 \
    --ImageUrl https://demo.com/resume.jpg \
    --SelectModel 1
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "Response": [
            {
                "Answer": "主要课程及成绩：港口机械发动机构造与维修1（60分）、钳工（85分）、底盘构造与维修（79分）、港口机械发动机构造与维修2（60分）、机械制图（84分）、液压与液力传动（84分）、数学（80分）、机械基础（79分）、艺术欣赏（90分）、历史（82分）、港口机械底盘构造与维修1（60分）、体育（81分）、管理学基础（80分）、港口机械底盘构造与维修（60分）、计算机应用（65分）",
                "QueryInfo": "根据图片内容，总结提炼课程的核心信息，字数精简，只总结图片上有的信息，不要做其他增添。若课程与图片内容毫无相关性，则输出：无相关内容"
            }
        ],
        "RequestId": "e0c8e1fb-d83c-44b9-b260-5bdeefbbe32d"
    }
}
```

**Example 5: QueryType=4信息提取**

提取简历图的字段

Input: 

```
tccli ocr RecognizeAgent --cli-unfold-argument  \
    --QueryType 4 \
    --ImageUrl https://demo.com/form.jpg \
    --SchemaItems.0.KeyName 姓名 \
    --SchemaItems.0.KeyType 0 \
    --SchemaItems.0.KeyPrompt 具体名字 \
    --SchemaItems.1.KeyName 出生年月 \
    --SchemaItems.1.KeyType 0 \
    --SchemaItems.1.KeyPrompt 如，2026年1月 \
    --SchemaItems.2.KeyName 主要课程 \
    --SchemaItems.2.KeyType 1 \
    --SchemaItems.2.KeyPrompt 课程列表，有课程名称，以及成绩 \
    --SchemaItems.2.SubItems.0.KeyName 课程 \
    --SchemaItems.2.SubItems.0.KeyType 0 \
    --SchemaItems.2.SubItems.0.KeyPrompt 课程名称，如政治 \
    --SchemaItems.2.SubItems.1.KeyName 成绩 \
    --SchemaItems.2.SubItems.1.KeyType 0 \
    --SchemaItems.2.SubItems.1.KeyPrompt 具体分数，如99 \
    --SelectModel 0
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "RequestId": "d8fe42e3-1b3d-46dc-9784-2eadf081e34a",
        "Response": [
            {
                "ExtractFields": [
                    {
                        "KeyName": "姓名",
                        "KeyPrompt": "具体名字",
                        "KeyType": 0,
                        "KeyValue": "王臣"
                    },
                    {
                        "KeyName": "出生年月",
                        "KeyPrompt": "如，2026年1月",
                        "KeyType": 0,
                        "KeyValue": "2005年1月"
                    },
                    {
                        "KeyName": "主要课程",
                        "KeyPrompt": "课程列表，有课程名称，以及成绩",
                        "KeyType": 1,
                        "SubItems": [
                            {
                                "Groups": [
                                    {
                                        "KeyName": "课程",
                                        "KeyPrompt": "课程名称，如政治",
                                        "KeyType": 0,
                                        "KeyValue": "底盘构造与维修"
                                    },
                                    {
                                        "KeyName": "成绩",
                                        "KeyPrompt": "具体分数，如99",
                                        "KeyType": 0,
                                        "KeyValue": "79"
                                    }
                                ]
                            },
                            {
                                "Groups": [
                                    {
                                        "KeyName": "课程",
                                        "KeyPrompt": "课程名称，如政治",
                                        "KeyType": 0,
                                        "KeyValue": "钳工"
                                    },
                                    {
                                        "KeyName": "成绩",
                                        "KeyPrompt": "具体分数，如99",
                                        "KeyType": 0,
                                        "KeyValue": "85"
                                    }
                                ]
                            },
                            {
                                "Groups": [
                                    {
                                        "KeyName": "课程",
                                        "KeyPrompt": "课程名称，如政治",
                                        "KeyType": 0,
                                        "KeyValue": "港口机械发动机构造与维修1"
                                    },
                                    {
                                        "KeyName": "成绩",
                                        "KeyPrompt": "具体分数，如99",
                                        "KeyType": 0,
                                        "KeyValue": "60"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

