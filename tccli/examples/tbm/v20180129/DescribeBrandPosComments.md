**Example 1: 查看品牌的用户好评观点列表**



Input: 

```
tccli tbm DescribeBrandPosComments --cli-unfold-argument  \
    --BrandId qijGLCi6bE0weVWgO7fjvfo4Wvo9kfzujw%3D%3D \
    --StartDate 2018-01-02 \
    --EndDate 2018-01-04 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BrandCommentSet": [
            {
                "Comment": "还行，质量过关",
                "Date": "2018-01-04 00:00:00"
            },
            {
                "Comment": "一般吧，下次做更好",
                "Date": "2018-01-04 00:00:00"
            },
            {
                "Comment": "比我之前买的厚实很多",
                "Date": "2018-01-04 00:00:00"
            },
            {
                "Comment": "不错不错",
                "Date": "2018-01-04 00:00:00"
            }
        ],
        "RequestId": "578794b0-127a-4dac-9044-0ba0ef026b15",
        "TotalComments": 25
    }
}
```

