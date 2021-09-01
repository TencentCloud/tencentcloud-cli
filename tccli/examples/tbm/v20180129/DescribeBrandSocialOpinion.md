**Example 1: 查看品牌用户观点列表**



Input: 

```
tccli tbm DescribeBrandSocialOpinion --cli-unfold-argument  \
    --BrandId qijGLCi6bE0weVWgO7fjvfo4Wvo9kfzujw%3D%3D \
    --StartDate 2018-02-01 \
    --EndDate 2018-02-10 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ArticleCount": 31,
        "FromCount": 1,
        "AdverseCount": 2,
        "ArticleSet": [
            {
                "FromSite": "",
                "PubTime": "2018-02-10 13:00:00",
                "Title": "test",
                "Url": "",
                "ArticleId": "qijGLCi6bE0weVWgO7fjvfo4Wvo9kfzujwoo",
                "Flag": 0,
                "Hot": 1,
                "Level": 2,
                "Abstract": "摘要"
            }
        ],
        "RequestId": "aaf3c86d-c143-4476-af5b-4d89ebc0f410"
    }
}
```

