**Example 1: 获取模板 ID 为 30 的内容审核模板**

获取模板 ID 为 30 的内容审核模板

Input: 

```
tccli vod DescribeContentReviewTemplates --cli-unfold-argument  \
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
                "Name": "模板1",
                "Comment": "内容审核模板",
                "ReviewWallSwitch": "ON",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "porn"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "bloody"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "OcrReviewInfo": {
                        "Switch": "OFF",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "politician"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "ProhibitedConfigure": null,
                "UserDefineConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "ScreenshotInterval": 1,
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

**Example 2: 获取指定个数的内容审核模板**

从序号 0 开始，获取 10 个内容审核模板，包括系统默认内容审核模板。

Input: 

```
tccli vod DescribeContentReviewTemplates --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "ContentReviewTemplateSet": [
            {
                "Definition": 30,
                "Name": "模板1",
                "Comment": "内容审核模板",
                "ReviewWallSwitch": "ON",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "porn"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "bloody"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "OcrReviewInfo": {
                        "Switch": "OFF",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "politician"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "ProhibitedConfigure": null,
                "UserDefineConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "ScreenshotInterval": 1,
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            },
            {
                "Definition": 31,
                "Name": "模板2",
                "Comment": "内容审核模板",
                "ReviewWallSwitch": "ON",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "OFF"
                    },
                    "AsrReviewInfo": {
                        "Switch": "OFF"
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "OcrReviewInfo": {
                        "Switch": "OFF",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "politician"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "ProhibitedConfigure": null,
                "UserDefineConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "ScreenshotInterval": 1,
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

