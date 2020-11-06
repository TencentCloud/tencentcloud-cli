**Example 1: 获得定制的行业相关报道**



Input: 

```
tccli tbm DescribeIndustryNews --cli-unfold-argument  \
    --IndustryId qijGLCi6bE0weVWrJ7L4qgm5nxET0u0Y9XwF \
    --StartDate 2018-02-1 \
    --EndDate 2018-02-10 \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NewsCount": 152,
        "FromCount": 1,
        "AdverseCount": 2,
        "DateCountSet": [
            {
                "Count": 3,
                "Date": "2018-07-07"
            },
            {
                "Count": 0,
                "Date": "2018-07-08"
            },
            {
                "Count": 0,
                "Date": "2018-07-09"
            },
            {
                "Count": 2,
                "Date": "2018-07-10"
            }
        ],
        "NewsSet": [
            {
                "FromSite": "且逛",
                "PubTime": "2018-02-09 10:32:07",
                "Title": "三张图带你看懂 腾讯新零售生态的布局",
                "Url": "http://mp.weixin.qq.com/s?__biz=MzI1MzczMDQzNg==&mid=2247483907&idx=1&sn=91deced0aff67a2143bc3cbccbfae0a6&chksm=e9d149e8dea6c0fe661426638396a05fb7fc5c8adf5cac07157f93e31d2613483b196ddd754d#rd",
                "Hot": 1,
                "Level": 2,
                "Flag": 0,
                "Abstract": "摘要"
            }
        ],
        "RequestId": "02363e3b-b048-40df-aaeb-8ec0f449e525"
    }
}
```

