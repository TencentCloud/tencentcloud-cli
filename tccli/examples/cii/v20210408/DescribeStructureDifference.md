**Example 1: 结构化对比查询接口示例**



Input: 

```
tccli cii DescribeStructureDifference --cli-unfold-argument  \
    --MainTaskId fybnnac89vk \
    --SubTaskId 
```

Output: 
```
{
    "Response": {
        "MainTaskId": "fybnnac89vk",
        "Status": 0,
        "Results": [
            {
                "SubTaskId": "Snz0ypwht1xd",
                "TaskType": "BUltrasoundReport",
                "ModifyItems": [
                    {
                        "Path": "detailInfo/desc/organs/imageFeature/src",
                        "Machine": "回声",
                        "Manual": "回声均匀"
                    }
                ],
                "NewItems": [
                    {
                        "Path": "detailInfo/summary/syms/attrs/性质",
                        "Value": "{\"__key\":\"f8ycfblrrh8\",\"desc\":\"性质\",\"indexChar\":-1,\"indexRow\":-1,\"positive\":\"\",\"src\":\"\",\"type\":\"\",\"value\":\"测试888888\"}"
                    }
                ],
                "RemoveItems": [
                    {
                        "Path": "detailInfo/desc/organs/sizes",
                        "Value": "[{\"__key\":\"nz0yrpr2ux4\",\"desc\":\"\",\"indexChar\":130,\"indexRow\":0,\"numbers\":[29],\"src\":\"厚2.9CM\",\"type\":\"厚\",\"unit\":\"MM\",\"value\":\"厚2.9CM\"}]"
                    }
                ]
            }
        ],
        "RequestId": "6e2f2787-1851-4bf1-8477-08c93b6ee652"
    }
}
```

