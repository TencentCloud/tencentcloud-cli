**Example 1: 基线分类**



Input: 

```
tccli cwp DescribeBaselineRuleCategoryList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CategoryId": 1,
                "ParentCategoryId": 0,
                "CategoryName": "等保合规"
            },
            {
                "CategoryId": 3,
                "ParentCategoryId": 0,
                "CategoryName": "未授权访问"
            },
            {
                "CategoryId": 4,
                "ParentCategoryId": 0,
                "CategoryName": "弱口令"
            },
            {
                "CategoryId": 5,
                "ParentCategoryId": 0,
                "CategoryName": "远程代码执行"
            },
            {
                "CategoryId": 6,
                "ParentCategoryId": 0,
                "CategoryName": "其他"
            },
            {
                "CategoryId": 7,
                "ParentCategoryId": 0,
                "CategoryName": "腾讯云安全标准"
            }
        ],
        "RequestId": "0be3d997-550d-4762-8a6e-243994719407"
    }
}
```

