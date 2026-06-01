**Example 1: 测试示例**



Input: 

```
tccli tchousex DescribeEngineRegions --cli-unfold-argument  \
    --Product abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "TotalCount": 0,
        "RegionSet": [
            {
                "Region": "abc",
                "RegionName": "abc",
                "RegionState": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

