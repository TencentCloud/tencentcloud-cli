**Example 1: 获取系统分类树**

获取系统分类树

Input: 

```
tccli csip DescribeBaselineSystemCategoryList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SystemCategoryList": [
            {
                "Category": {
                    "CheckAssetType": "HOST",
                    "Description": "等保合规",
                    "ID": 1,
                    "Name": "等保合规"
                },
                "SubCategoryList": [
                    {
                        "Category": {
                            "CheckAssetType": "HOST",
                            "Description": "等保二级-CentOS 6安全基线检查",
                            "ID": 23,
                            "Name": "等保二级-CentOS 6安全基线检查"
                        }
                    }
                ]
            }
        ],
        "RequestId": "e5d75fb1-e878-455f-b630-392a7e87d020"
    }
}
```

