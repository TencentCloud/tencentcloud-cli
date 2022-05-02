**Example 1: DescribeTsRegion**



Input: 

```
tccli waf DescribeTsRegion --cli-unfold-argument  \
    --MainRegion bj \
    --SubRegion bj-0 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "b71d47f4-5882-4e59-9624-7041bd7314a6",
        "Count": 1,
        "Data": [
            {
                "Id": 2,
                "MainRegion": "bj",
                "SubRegion": "bj-0",
                "DomainCount": 0,
                "CreateTime": "2021-12-02T20:31:14+08:00"
            }
        ]
    }
}
```

