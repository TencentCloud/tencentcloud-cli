**Example 1: 获取视图详情**



Input: 

```
tccli cloudrc GetView --cli-unfold-argument  \
    --ViewId vw-6wyborpx
```

Output: 
```
{
    "Response": {
        "ViewId": "vw-6wyborpx",
        "ViewName": "后付费资源视图",
        "ConditionRule": {
            "Type": "complex",
            "ComplexOption": "and",
            "ComplexArray": [
                {
                    "Type": "simple",
                    "SimpleKey": "PayMode",
                    "SimpleOption": "equals",
                    "SimpleValue": [
                        "0"
                    ]
                }
            ]
        },
        "Tags": [
            {
                "Key": "部门",
                "Value": "开发部"
            }
        ],
        "ViewCreateTime": "2024-03-24 16:36:54",
        "ViewUpdateTime": "2024-03-24 16:36:54",
        "RequestId": "52a404c5-fd9c-4f28-8ef4-54fda03b3b13"
    }
}
```

**Example 2: 获取不存在的视图详情**



Input: 

```
tccli cloudrc GetView --cli-unfold-argument  \
    --ViewId vw-notexits
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.ViewIdNotFound",
            "Message": "视图ID不存在"
        },
        "RequestId": "10ca642a-2a18-42ec-ae35-cb086c21f35a"
    }
}
```

