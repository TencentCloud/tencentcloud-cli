**Example 1: 查看品牌的用户差评观点列表**



Input: 

```
tccli tbm DescribeBrandNegComments --cli-unfold-argument  \
    --BrandId qijGLCi6bE0weVWgO7fjvfo4Wvo9kfzujw%3D%3D \
    --StartDate 2018-02-21 \
    --EndDate 2018-02-22 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BrandCommentSet": [
            {
                "Comment": "不会吧，这也行吗",
                "Date": "2018-02-22 00:00:00"
            },
            {
                "Comment": "不喜欢",
                "Date": "2018-02-22 00:00:00"
            },
            {
                "Comment": "太不安全了，简直无视用户",
                "Date": "2018-02-21 00:00:00"
            }
        ],
        "RequestId": "8fdd4c33-600c-4ec7-be16-c2cd4f6d4121",
        "TotalComments": 6
    }
}
```

