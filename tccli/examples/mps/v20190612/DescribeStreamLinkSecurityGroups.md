**Example 1: 请求示例**

批量查询安全组信息。

Input: 

```
tccli mps DescribeStreamLinkSecurityGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Id": "abc",
                "Name": "abc",
                "Whitelist": [
                    "abc"
                ],
                "OccupiedInputs": [
                    "abc"
                ],
                "Region": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

