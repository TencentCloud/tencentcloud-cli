**Example 1: 查询示例**



Input: 

```
tccli waf DescribeCdcResource --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values 1 \
    --Filters.0.Name Status \
    --Filters.0.ExactMatch False \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "Status": 0,
                "Ip": "11.164.128.10",
                "ClusterId": "cluster-o41khj15",
                "Auth": "VGNkbjIwMTc2",
                "Id": 1,
                "OpAppId": 1300899512,
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "Port": 6889,
                "Type": "slave-redis",
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2"
    }
}
```

