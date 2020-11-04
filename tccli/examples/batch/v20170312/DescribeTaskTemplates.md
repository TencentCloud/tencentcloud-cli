**Example 1: 查询任务模板**



Input: 

```
tccli batch DescribeTaskTemplates --cli-unfold-argument  \
    --TaskTemplateIds task-tmpl-pq24rq1e task-tmpl-606i415o
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TaskTemplateSet": [
            {
                "TaskTemplateName": "rendering",
                "TaskTemplateDescription": "3ds Max 2018 Demo",
                "TaskTemplateId": "task-tmpl-pq24rq1e",
                "CreateTime": "2018-03-08T03:27:43Z",
                "Tags": [
                    {
                        "Key": "batch-test-tag-tp-key",
                        "Value": "batch-test-tag-tp-value"
                    }
                ],
                "TaskTemplateInfo": {
                    "OutputMappings": [
                        {
                            "SourcePath": "C:\\\\render\\\\",
                            "DestinationPath": "cos://bucket-appid.cos.ap-guangzhou.myqcloud.com/"
                        }
                    ],
                    "TaskInstanceNum": 1,
                    "ComputeEnv": {
                        "EnvType": "MANAGED",
                        "EnvData": {
                            "SystemDisk": {
                                "DiskSize": "50",
                                "DiskType": "CLOUD_BASIC"
                            },
                            "LoginSettings": {
                                "Password": "B1habcdB1habcd"
                            },
                            "InternetAccessible": {
                                "InternetMaxBandwidthOut": "10",
                                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR"
                            },
                            "ImageId": "img-i64lx84h",
                            "InstanceType": "S1.LARGE8",
                            "DataDisks": [
                                {
                                    "DiskSize": "0",
                                    "DiskType": "CLOUD_BASIC"
                                }
                            ]
                        }
                    },
                    "RedirectInfo": {
                        "StdoutRedirectPath": "cos://bucket-appid.cos.ap-guangzhou.myqcloud.com/wonderflet/logs/",
                        "StderrRedirectPath": "cos://bucket-appid.cos.ap-guangzhou.myqcloud.com/wonderflet/logs/"
                    },
                    "Application": {
                        "Command": "3dsmaxcmd Demo.max -outputName:c:\\\\render\\\\image.jpg",
                        "PackagePath": "cos://bucket-appid.cos.ap-guangzhou.myqcloud.com/render/max.tar.gz",
                        "DeliveryForm": "PACKAGE"
                    },
                    "MaxRetryCount": 0,
                    "Timeout": 259200,
                    "FailedAction": "TERMINATE",
                    "TaskName": "rendering"
                }
            },
            {
                "TaskTemplateName": "A",
                "TaskTemplateDescription": "",
                "TaskTemplateId": "task-tmpl-606i415o",
                "CreateTime": "2018-01-25T07:46:12Z",
                "Tags": [
                    {
                        "Key": "batch-test-tag-tp-key",
                        "Value": "batch-test-tag-tp-value"
                    }
                ],
                "TaskTemplateInfo": {
                    "TaskInstanceNum": 2,
                    "ComputeEnv": {
                        "EnvType": "MANAGED",
                        "EnvData": {
                            "InstanceType": "S1.SMALL1",
                            "ImageId": "img-bq1gnde2"
                        }
                    },
                    "RedirectInfo": {
                        "StdoutRedirectPath": "cos://bucket-appid.cos.ap-guangzhou.myqcloud.com/hello2/logs/",
                        "StderrRedirectPath": "cos://bucket-appid.cos.ap-guangzhou.myqcloud.com/hello2/logs/"
                    },
                    "Application": {
                        "Command": "python -c \"fib=lambda n:1 if n&lt=2 else fib(n-1)+fib(n-2); print(fib(20))\" ",
                        "DeliveryForm": "LOCAL"
                    },
                    "MaxRetryCount": 0,
                    "FailedAction": "TERMINATE",
                    "TaskName": "A"
                }
            }
        ],
        "RequestId": "23f7d202-1cd4-4658-a989-88ad4ed77aac"
    }
}
```

