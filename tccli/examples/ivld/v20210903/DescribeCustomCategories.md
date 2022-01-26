**Example 1: 未创建任何分类，返回空数组**



Input: 

```
tccli ivld DescribeCustomCategories --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CategorySet": [],
        "RequestId": "d8461ee7-c4eb-429e-8609-3fa727e5f064"
    }
}
```

**Example 2: 描述自定义人物类型**



Input: 

```
tccli ivld DescribeCustomCategories --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CategorySet": [
            {
                "CategoryId": "13",
                "L1Category": "公众人物",
                "L2Category": "知名律师"
            }
        ],
        "RequestId": "2759b810-ad36-4936-93b4-7b374a878e6a"
    }
}
```

