**Example 1: 获取指定个数的智能审核模板**

从序号 0 开始，获取 10 个智能审核模板，包括系统默认智能审核模板。

Input: 

```
tccli mps DescribeContentReviewTemplates --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ContentReviewTemplateSet": [
            {
                "Definition": 10,
                "Name": "智能模板1",
                "Comment": "智能模板1说明",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label1"
                        ],
                        "BlockConfidence": 90,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label2"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label3"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "ProhibitedConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "UserDefineConfigure": {
                    "FaceReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label4"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label5"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label6"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "CreateTime": "2019-04-24T07:28:03+08:00",
                "UpdateTime": "2019-04-24T07:28:03+08:00",
                "Type": "Preset"
            }
        ],
        "RequestId": "008xxxxx-xxxx-xxxx-xxxx-xxxxxxxxaa48"
    }
}
```

**Example 2: 获取模板 ID 为 30 的智能审核模板**



Input: 

```
tccli mps DescribeContentReviewTemplates --cli-unfold-argument  \
    --Definitions 30
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ContentReviewTemplateSet": [
            {
                "Definition": 30,
                "Name": "智能模板1",
                "Comment": "智能模板1说明",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label1"
                        ],
                        "BlockConfidence": 90,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label2"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label3"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "ProhibitedConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "UserDefineConfigure": {
                    "FaceReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label4"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label5"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "label6"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "CreateTime": "2019-04-24T07:28:03+08:00",
                "UpdateTime": "2019-04-24T07:28:03+08:00",
                "Type": "Preset"
            }
        ],
        "RequestId": "008xxxxx-xxxx-xxxx-xxxx-xxxxxxxxaa48"
    }
}
```

