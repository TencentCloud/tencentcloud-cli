**Example 1: 查询推理镜像模板**



Input: 

```
tccli tione DescribeInferTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FrameworkTemplates": [
            {
                "Framework": "TENSORFLOW",
                "FrameworkVersion": "2.4",
                "Groups": [
                    "TENSORFLOW",
                    "LIGHT"
                ],
                "InferTemplates": [
                    {
                        "InferTemplateId": "tf2.4-py38-cpu",
                        "InferTemplateImage": "ccr.ccs.tencentyun.com/qcloud-ti-platform/ti-cloud-infer-tensorflow-cpu:py38-tensorflow2.4-cpu-20211206"
                    },
                    {
                        "InferTemplateId": "tf2.4-py38-gpu",
                        "InferTemplateImage": "ccr.ccs.tencentyun.com/qcloud-ti-platform/ti-cloud-infer-tensorflow-gpu:py38-tensorflow2.4-cu110-20211206"
                    }
                ]
            },
            {
                "Framework": "TENSORFLOW",
                "FrameworkVersion": "1.15",
                "Groups": [
                    "TENSORFLOW",
                    "LIGHT"
                ],
                "InferTemplates": [
                    {
                        "InferTemplateId": "tf1.15-py36-cpu",
                        "InferTemplateImage": "ccr.ccs.tencentyun.com/qcloud-ti-platform/ti-cloud-infer-tensorflow-cpu:py36-tensorflow1.15-cpu-20211206"
                    },
                    {
                        "InferTemplateId": "tf1.15-py36-gpu",
                        "InferTemplateImage": "ccr.ccs.tencentyun.com/qcloud-ti-platform/ti-cloud-infer-tensorflow-gpu:py36-tensorflow1.15-cu100-20211206"
                    }
                ]
            },
            {
                "Framework": "PYTORCH",
                "FrameworkVersion": "1.9",
                "Groups": [
                    "PYTORCH",
                    "LIGHT"
                ],
                "InferTemplates": [
                    {
                        "InferTemplateId": "py1.9.0-py36-cpu",
                        "InferTemplateImage": "ccr.ccs.tencentyun.com/qcloud-ti-platform/ti-cloud-infer-pytorch-cpu:py36-torch1.9.0-cpu-20211206"
                    },
                    {
                        "InferTemplateId": "py1.9.0-py36-cu111",
                        "InferTemplateImage": "ccr.ccs.tencentyun.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py36-torch1.9.0-cu111-20211206"
                    }
                ]
            },
            {
                "Framework": "PMML",
                "FrameworkVersion": "0.9.12",
                "Groups": [
                    "SPARK",
                    "PYSPARK"
                ],
                "InferTemplates": [
                    {
                        "InferTemplateId": "pmml-py36",
                        "InferTemplateImage": "ccr.ccs.tencentyun.com/qcloud-ti-platform/ti-cloud-infer-pmml:py36-pmml-20211206"
                    }
                ]
            }
        ],
        "RequestId": "b53d7b75-e61b-4b0f-9c28-60ed06f5caeb"
    }
}
```

