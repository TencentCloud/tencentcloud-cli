**Example 1: 获取品牌的总热度值**



Input: 

```
tccli tbm DescribeBrandExposure --cli-unfold-argument  \
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
                "Count": 698,
                "Date": "2018-01-24"
            },
            {
                "Count": 3502,
                "Date": "2018-01-25"
            },
            {
                "Count": 10432,
                "Date": "2018-01-26"
            },
            {
                "Count": 183,
                "Date": "2018-01-27"
            },
            {
                "Count": 529,
                "Date": "2018-01-28"
            },
            {
                "Count": 139,
                "Date": "2018-01-29"
            },
            {
                "Count": 281,
                "Date": "2018-01-30"
            },
            {
                "Count": 3664,
                "Date": "2018-01-31"
            },
            {
                "Count": 727,
                "Date": "2018-02-01"
            }
        ],
        "RequestId": "49589f39-66e4-4b04-82a5-8267da8c8e14",
        "TotalCount": 20155
    }
}
```

