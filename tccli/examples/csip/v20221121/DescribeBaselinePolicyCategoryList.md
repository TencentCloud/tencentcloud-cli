**Example 1: 获取策略系统配置分类**

获取策略系统配置分类

Input: 

```
tccli csip DescribeBaselinePolicyCategoryList --cli-unfold-argument  \
    --PolicyID 2 \
    --MemberId mem-**********5795752f66e429
```

Output: 
```
{
    "Response": {
        "SystemCategoryList": [
            {
                "Category": {
                    "CheckAssetType": "HOST",
                    "Description": "自定义基线检查",
                    "ID": 8,
                    "Name": "自定义基线"
                },
                "ItemCount": 2,
                "SubCategoryList": [
                    {
                        "Category": {
                            "CheckAssetType": "HOST",
                            "Description": "CentOS7/8自定义基线检查",
                            "ID": 159,
                            "Name": "CentOS7/8自定义基线检查"
                        }
                    }
                ]
            }
        ],
        "RequestId": "d5139977-0d70-482a-b30d-4abdc74b3869"
    }
}
```

