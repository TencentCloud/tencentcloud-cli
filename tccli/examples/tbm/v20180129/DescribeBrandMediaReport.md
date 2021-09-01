**Example 1: 查看品牌资讯报道数量**



Input: 

```
tccli tbm DescribeBrandMediaReport --cli-unfold-argument  \
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
                "Count": 600,
                "Date": "2018-01-24"
            },
            {
                "Count": 3231,
                "Date": "2018-01-25"
            },
            {
                "Count": 10030,
                "Date": "2018-01-26"
            },
            {
                "Count": 32,
                "Date": "2018-01-27"
            },
            {
                "Count": 48,
                "Date": "2018-01-28"
            },
            {
                "Count": 17,
                "Date": "2018-01-29"
            },
            {
                "Count": 75,
                "Date": "2018-01-30"
            },
            {
                "Count": 3195,
                "Date": "2018-01-31"
            },
            {
                "Count": 694,
                "Date": "2018-02-01"
            }
        ],
        "RequestId": "b8edf4f1-5d24-493c-b51b-95ff681b218f",
        "TotalCount": 17922
    }
}
```

