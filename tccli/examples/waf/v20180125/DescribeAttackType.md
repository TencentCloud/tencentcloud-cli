**Example 1: 查询Bot数量**



Input: 

```
tccli waf DescribeAttackType --cli-unfold-argument  \
    --Host www.test.com \
    --FromTime '2020-02-24 00:00:00' \
    --ToTime '2020-02-24 19:00:00' \
    --Edition clb-waf
```

Output: 
```
{
    "Response": {
        "RequestId": "9ee8be5b-6caa-4c39-ab70-890e0e673515",
        "Piechart": []
    }
}
```

