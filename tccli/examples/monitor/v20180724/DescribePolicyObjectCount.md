**Example 1: 查询策略组在每个地域下面绑定的对象数统计**



Input: 

```
tccli monitor DescribePolicyObjectCount --cli-unfold-argument  \
    --Module monitor \
    --GroupId 111
```

Output: 
```
{
    "Response": {
        "IsMultiRegion": true,
        "RegionList": [
            {
                "Count": 0,
                "Region": "th"
            },
            {
                "Count": 0,
                "Region": "usw"
            },
            {
                "Count": 0,
                "Region": "in"
            },
            {
                "Count": 0,
                "Region": "ru"
            },
            {
                "Count": 0,
                "Region": "sh"
            },
            {
                "Count": 1,
                "Region": "gz"
            },
            {
                "Count": 0,
                "Region": "hzec"
            },
            {
                "Count": 0,
                "Region": "jp"
            },
            {
                "Count": 0,
                "Region": "kr"
            },
            {
                "Count": 0,
                "Region": "nj"
            },
            {
                "Count": 0,
                "Region": "shjr"
            },
            {
                "Count": 0,
                "Region": "szjr"
            },
            {
                "Count": 0,
                "Region": "tsn"
            },
            {
                "Count": 0,
                "Region": "ca"
            },
            {
                "Count": 0,
                "Region": "gzopen"
            },
            {
                "Count": 0,
                "Region": "jnec"
            },
            {
                "Count": 0,
                "Region": "de"
            },
            {
                "Count": 0,
                "Region": "hk"
            },
            {
                "Count": 0,
                "Region": "sg"
            },
            {
                "Count": 0,
                "Region": "use"
            },
            {
                "Count": 0,
                "Region": "bj"
            },
            {
                "Count": 0,
                "Region": "cd"
            },
            {
                "Count": 0,
                "Region": "cq"
            }
        ],
        "RequestId": "853dafdc-22d4-4e9d-88a7-ebc43abf7cef"
    }
}
```

