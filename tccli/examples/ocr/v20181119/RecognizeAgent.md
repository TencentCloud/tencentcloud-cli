**Example 1: QueryType=0全文识别**

识别且输出全文内容

Input: 

```
tccli ocr RecognizeAgent --cli-unfold-argument  \
    --QueryType 0 \
    --ImageUrl https://demo-1400073141.cos.ap-guan***o*.myqcloud.com/10.%20image2.jpg*q-sign-a**orithm=sha1&q-ak=AKID**vZ0eN6*j2NsBQJn7TdtNs1K0*l*Jn8i**E*aEKREeZimpybAs***bVG1Aoot*n&q-sign-time=177*824**1;1776*28351&q-key-time=17**824751**776828351&q-header-l*s******&q-url-param-list=&q-signature=83bb8ce9c768fde565e71b0460e6dbde1b4886f4&x-cos-security-token=xheG1dXFML3tXG5BbL3WBkxVgTMPn53a305890e6c04febe60e215a5a32833a69POGPBv-E8gHNUZW60alPmkc4RfdRY-_t8Ui8YDNXe1cYF6_ToPvP6_zzdNrdcV7IFK2puDFJESTWb5bpdgNFzBYaIqMBzQ5mGNamTbS3zRP0FMQTNpGj-3aq5Y0Nq46WuYcs4KcX29RE6LuZeuUo9ODhoWjqS69N4MmunTB2fJwpu9GqgkKpLu98DaKKIFpxF_12tfVf4_RuH1xbATmJAMl4h1-ni7Ga25th3WlWlDgJ1WE15lVSJueMoPdmbNvvOQBuBl4zTGtc3AEy3MFKmg \
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
    --ImageUrl https://demo-1400073141.cos.ap-guangzhou.myqcloud.com/10.%20image2.j**?***ign-algorithm=sha1&q***=AKIDK8Gu4gzUbrOpn8kb39mD*i594DkHgNJrrT20ogVq5WW0-hTRR*MP***S*Yn*_*Y*&q-sign-time=1**6*50064;17767**664&q-key-tim*=1*7**5*0****77*753664&q-head**-list=host&q*url-param-list=&*-*ignatur**2936fe3e8fb70d0883100e*2*e9e829b83e6cd79&x-cos-security-token=2h4y82Xge6IaO54EmvE4bkv7jnUKzcHa60478ede97391b5c9812986943e6b2b4VQOPSF0rD_E_hBrKn29TH08ObJC1ujL1EVTKrbVHKYxip6a1Sm9GrhNz9KuYTG4V9BJ_RptFea1UUlABknv0GNlp-0tr23g2t7-WMtZTxfS0kCDsQoXiq-t1Egh5uXxoLzqM8XWJv6KG4jSi3mG4jGkDoefVlbh680uYMGkmSTHDMTUDQ-1kpsJcPr2N7JmBQ1Dr2VrMbFnvLz2GE5hQHQjuo54MUZoXSA_evrJXegbWREY01E_sLHNMv9E-SG_UzSPMuX9wnJPJioo7CAg6vg \
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
    --ImageUrl https://demo-1400073141.cos.ap-guangzhou.myqcloud.com/%E5%A2%9E%E5%80%BC%E7%A8%8E%E5%8F%91%E7%A5%A8.png?q-sign-algorithm=sha1&q-ak=AKID4-Xu1TJlFcWCFYFcBM0jeYFhiLideyQNzjB1-auWplOZvevH7dhYJUmvalPjJxQj&q-sign-time=1776751051;1776754651&q-key-time=1776751051;1776754651&q-header-list=host&q-url-param-list=&q-signature=b23789a5890773068358aeb44139438305476ecd&x-cos-security-token=2h4y82Xge6IaO54EmvE4bkv7jnUKzcHa8319cf620e8171067cc7ef6ca8617822VQOPSF0rD_E_hBrKn29TH5h5D0EhOeBXrfHCLSAbyKOB4y6kKOr6cv8ytWL3KQ8ROGETurrABAoOBjogE9jrCksk5xn0GOuHmFdFAmUXibaI6mHHLIuN8MZf7u-_CaKnBoRVWVTitlJ2_QJGC01pfhWwirM30MMMiKMZnZ5GnBX3duGLkFIF4THWxpX_XxmVkA2567rXs315V3viCAww83Xs7aYRWqt7R89Gj0HDIPfGLhsNZcUVedZw1vsvqovzjRibsRrfGWRajQ4qcx11ig \
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
    --ImageUrl https://demo-1400073141.cos.ap-guangzhou.myqcloud.com/10.%20image2.jpg?q-sign-algorithm=sha1&q-ak=AKIDWyvZ0eN6uj2NsBQJn7TdtNs1K05lLJn8ihMENaEKREeZimpybAsYuRbVG1Aootln&q-sign-time=1776824751;1776828351&q-key-time=1776824751;1776828351&q-header-list=host&q-url-param-list=&q-signature=83bb8ce9c768fde565e71b0460e6dbde1b4886f4&x-cos-security-token=xheG1dXFML3tXG5BbL3WBkxVgTMPn53a305890e6c04febe60e215a5a32833a69POGPBv-E8gHNUZW60alPmkc4RfdRY-_t8Ui8YDNXe1cYF6_ToPvP6_zzdNrdcV7IFK2puDFJESTWb5bpdgNFzBYaIqMBzQ5mGNamTbS3zRP0FMQTNpGj-3aq5Y0Nq46WuYcs4KcX29RE6LuZeuUo9ODhoWjqS69N4MmunTB2fJwpu9GqgkKpLu98DaKKIFpxF_12tfVf4_RuH1xbATmJAMl4h1-ni7Ga25th3WlWlDgJ1WE15lVSJueMoPdmbNvvOQBuBl4zTGtc3AEy3MFKmg \
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
    --ImageUrl https://demo-1400073141.cos.ap-guangzhou.myqcloud.com/10.%20image2.jpg?q-sign-algorithm=sha1&q-ak=AKIDyrWqLRrQ1Si19TU6ChKv5DLrPKFR77A08bhHdfoRqNgh_DetWbaFzNxDyQN3a9yh&q-sign-time=1776751694;1776755294&q-key-time=1776751694;1776755294&q-header-list=host&q-url-param-list=&q-signature=522cd0947c759fa4009f63966bee66db86ac4ef2&x-cos-security-token=2h4y82Xge6IaO54EmvE4bkv7jnUKzcHa0e6c6fb81df434070af64a0a8df5dfdcVQOPSF0rD_E_hBrKn29TH1-5bw1mGNKKOEOlkk-oOZ9t8PtjUi79GCHH6m2DNTkdd0-5fVKyM_EVPGdCNv0DJTB4lEHJcCafNflaZq-JD2EcUcfS118k6r09iTKm7gkyTZ95M_CsNj8UfISHcpx6XpDKShN_5NzJ7yjlWR2SYFmPvLaQHrOse4ErhU_MGkFcBYNk7igraUh31Bm79-s2rj75E0hIkiNDg_KxvmXJfc1Jdv0F-yXZkLN9PrpR6qp7iJR0Qp0FnAuyxtbxekob9g \
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

