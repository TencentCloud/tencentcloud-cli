**Example 1: 批量描述自定义人物**



Input: 

```
tccli ivld DescribeCustomPersons --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 15
```

Output: 
```
{
    "Response": {
        "PersonInfoSet": [],
        "RequestId": "802f88a4-3c8f-4aff-8328-bc7591fdacc1",
        "TotalCount": 0
    }
}
```

**Example 2: 成功批量描述人物信息**



Input: 

```
tccli ivld DescribeCustomPersons --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 50
```

Output: 
```
{
    "Response": {
        "PersonInfoSet": [
            {
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
            }
        ],
        "RequestId": "9f5bc011-fa0b-4ad9-a4a1-2481343e9428",
        "TotalCount": 1
    }
}
```

