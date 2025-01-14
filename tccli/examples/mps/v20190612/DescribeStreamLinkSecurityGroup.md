**Example 1: 请求示例**

查询安全组。

Input: 

```
tccli mps DescribeStreamLinkSecurityGroup --cli-unfold-argument  \
    --Id abc
```

Output: 
```
{
    "Response": {
        "Info": {
            "Id": "abc",
            "Name": "abc",
            "Whitelist": [
                "abc"
            ],
            "OccupiedInputs": [
                "abc"
            ],
            "Region": "abc"
        },
        "RequestId": "abc"
    }
}
```

