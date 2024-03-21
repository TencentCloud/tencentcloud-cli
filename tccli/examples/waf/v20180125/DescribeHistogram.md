**Example 1: 查询Bot数量**



Input: 

```
tccli waf DescribeHistogram --cli-unfold-argument  \
    --Host www.test.com \
    --FromTime '2019-12-30 00:00:00' \
    --ToTime '2019-12-31 00:00:00' \
    --Edition clb-waf \
    --QueryField ip \
    --Source 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9ee8be5b-6caa-4c39-ab70-890e0e673515",
        "Histogram": []
    }
}
```

