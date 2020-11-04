**Example 1: 查询自定义镜像制作进度**



Input: 

```
tccli bm DescribeCustomImageProcess --cli-unfold-argument  \
    --ImageId testid
```

Output: 
```
{
    "Response": {
        "RequestId": "cc8106bc-24a0-46a1-bffb-947bd5d6929f",
        "CustomImageProcessSet": [
            {
                "StepName": "制作前，检查系统环境",
                "StepType": 2,
                "StartTime": "2018-08-06 17:23:31"
            },
            {
                "StepName": "制作镜像中",
                "StepType": 1,
                "StartTime": "2018-08-06 17:41:54"
            },
            {
                "StepName": "制作完成，重启系统中",
                "StepType": 0,
                "StartTime": ""
            }
        ]
    }
}
```

