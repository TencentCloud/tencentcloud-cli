**Example 1: 获取某个应用下所有消息分类**



Input: 

```
tccli adp DescribeMsgRecordCategoryList --cli-unfold-argument  \
    --AppId 2062456131215815616
```

Output: 
```
{
    "Response": {
        "CategoryList": [
            {
                "CategoryId": "0",
                "Children": [
                    {
                        "CategoryId": "2087095266081654784",
                        "Children": [
                            {
                                "CategoryId": "2087095343458174976",
                                "Children": [],
                                "Name": "公众号渠道",
                                "Permission": {
                                    "CanAdd": true,
                                    "CanDelete": true,
                                    "CanEdit": true
                                },
                                "TotalCount": "0"
                            }
                        ],
                        "Name": "营销",
                        "Permission": {
                            "CanAdd": true,
                            "CanDelete": true,
                            "CanEdit": true
                        },
                        "TotalCount": "0"
                    }
                ],
                "Name": "全部分类",
                "Permission": {
                    "CanAdd": true,
                    "CanDelete": false,
                    "CanEdit": false
                },
                "TotalCount": "61"
            }
        ],
        "RequestId": "eae0d14b-8c50-46df-a791-0f449de920a3"
    }
}
```

