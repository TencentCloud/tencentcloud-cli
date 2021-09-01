**Example 1: 获取品牌在社交媒体上被报道的统计次数**



Input: 

```
tccli tbm DescribeBrandSocialReport --cli-unfold-argument  \
    --BrandId qijGLCi6bE0weVWgO7fjvfo4Wvo9kfzujw%3D%3D \
    --StartDate 2018-01-24 \
    --EndDate 2018-02-01
```

Output: 
```
{
    "Response": {
        "DateCountSet": [
            {
                "Count": 98,
                "Date": "2018-01-24"
            },
            {
                "Count": 271,
                "Date": "2018-01-25"
            },
            {
                "Count": 402,
                "Date": "2018-01-26"
            },
            {
                "Count": 151,
                "Date": "2018-01-27"
            },
            {
                "Count": 481,
                "Date": "2018-01-28"
            },
            {
                "Count": 122,
                "Date": "2018-01-29"
            },
            {
                "Count": 206,
                "Date": "2018-01-30"
            },
            {
                "Count": 469,
                "Date": "2018-01-31"
            },
            {
                "Count": 33,
                "Date": "2018-02-01"
            }
        ],
        "RequestId": "6574337a-ac0a-4f5f-8b03-a6a3b8281040",
        "TotalCount": 2233
    }
}
```

