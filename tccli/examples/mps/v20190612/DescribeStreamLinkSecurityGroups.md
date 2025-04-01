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
                "Id": "019202e96d9f09dc0f325e7f7a2a",
                "Name": "live_test",
                "Whitelist": [
                    "0.0.0.0"
                ],
                "OccupiedInputs": [
                    "01937702c54509dc0f3269ca341f"
                ],
                "Region": "ap-shanghai"
            }
        ],
        "RequestId": "019202e96d9f09dc0f325e7f7a2a"
    }
}
```

