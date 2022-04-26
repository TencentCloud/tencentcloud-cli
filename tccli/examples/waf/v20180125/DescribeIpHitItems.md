**Example 1: Waf  IP封堵状态查询**



Input: 

```
tccli waf DescribeIpHitItems --cli-unfold-argument  \
    --Domain www.test.com \
    --Category cc \
    --Skip 0 \
    --Limit 10 \
    --Sort ts_version:-1 \
    --Count 1 \
    --CtsMin 1578468704000 \
    --CtsMax 1578499199000
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [],
            "TotalCount": 0
        },
        "RequestId": "a4010dd1-d24b-43f5-bab4-8a6b204835b7"
    }
}
```

