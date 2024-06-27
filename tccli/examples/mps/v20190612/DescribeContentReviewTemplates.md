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
                "Definition": 0,
                "Name": "abc",
                "Comment": "abc",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "ProhibitedConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "UserDefineConfigure": {
                    "FaceReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Type": "abc"
            }
        ],
        "RequestId": "abc"
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
                "Definition": 0,
                "Name": "abc",
                "Comment": "abc",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "ProhibitedConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "UserDefineConfigure": {
                    "FaceReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "AsrReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    },
                    "OcrReviewInfo": {
                        "Switch": "abc",
                        "LabelSet": [
                            "abc"
                        ],
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Type": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

