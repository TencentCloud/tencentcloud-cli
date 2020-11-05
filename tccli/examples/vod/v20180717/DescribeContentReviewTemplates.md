**Example 1: Getting a specified number of content audit templates**

This example shows you how to get 10 video content audit templates with the serial number starting from 0, including the system default ones.

Input: 

```
tccli vod DescribeContentReviewTemplates --cli-unfold-argument  \
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "ContentReviewTemplateSet": [
            {
                "Definition": 30,
                "Name": "Template 1",
                "Comment": "Content audit template",
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
                "Name": "Template 2",
                "Comment": "Content audit template",
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

**Example 2: Getting the content audit template whose template ID is 30**

This example shows you how to get 10 video content audit templates with the serial number starting from 0, including the system default ones.

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
                "Name": "Template 1",
                "Comment": "Content audit template",
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

