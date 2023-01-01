**Example 1: 获取审核模板列表**

获取审核模板列表

Input: 

```
tccli vod DescribeReviewTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TotalCount": 1,
        "ReviewTemplateSet": [
            {
                "Comment": "过滤广告标签",
                "Definition": 10001,
                "UpdateTime": "2018-10-01T10:00:00Z",
                "Name": "过滤广告",
                "Labels": [
                    "Ads"
                ],
                "Type": "Custom",
                "CreateTime": "2018-10-01T10:00:00Z"
            }
        ]
    }
}
```

