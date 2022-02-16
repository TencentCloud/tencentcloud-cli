**Example 1: 成功描述人物详细信息(包括出现这个人物的任务ID列表)**



Input: 

```
tccli ivld DescribeCustomPersonDetail --cli-unfold-argument  \
    --PersonId person-Axgo3FYc
```

Output: 
```
{
    "Response": {
        "PersonInfo": {
            "BasicInfo": "测试基本信息",
            "CreateTime": "2022-01-25 10:35:47",
            "ImageInfoSet": [
                {
                    "ErrorCode": "OK",
                    "ErrorMsg": "OK",
                    "ImageId": "image-Axgo3FYc-egMN",
                    "ImageURL": "https://test-251202813.cos.ap-guangzhou.myqcloud.com/CustomImages/image-Axgo3FYc-egMN.jpeg"
                }
            ],
            "L1Category": "明星",
            "L2Category": "巨星",
            "Name": "测试姓名",
            "PersonId": "person-Axgo3FYc"
        },
        "RequestId": "db04f25b-0d68-4cba-9171-254abc8ff3ac",
        "TaskIdSet": []
    }
}
```

