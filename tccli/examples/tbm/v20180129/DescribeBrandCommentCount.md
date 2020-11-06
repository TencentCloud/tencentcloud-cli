**Example 1: 查看品牌的用户好评/差评数**



Input: 

```
tccli tbm DescribeBrandCommentCount --cli-unfold-argument  \
    --BrandId qijGLCi6bE0weVWgO7fjvfo4Wvo9kfzujw%3D%3D \
    --StartDate 2018-01-02 \
    --EndDate 2018-01-04
```

Output: 
```
{
    "Response": {
        "CommentSet": [
            {
                "Date": "2018-01-02",
                "NegCommentCount": 3,
                "PosCommentCount": 9
            },
            {
                "Date": "2018-01-03",
                "NegCommentCount": 1,
                "PosCommentCount": 5
            },
            {
                "Date": "2018-01-04",
                "NegCommentCount": 4,
                "PosCommentCount": 10
            }
        ],
        "RequestId": "1362f83b-c845-490e-bc81-49ee6ff8159b"
    }
}
```

