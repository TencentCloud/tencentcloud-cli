**Example 1: 请求示例**

查询安全组。

Input: 

```
tccli mps DescribeStreamLinkSecurityGroup --cli-unfold-argument  \
    --Id 019202e96d9f09dc0f325e7f7a2a
```

Output: 
```
{
    "Response": {
        "Info": {
            "Id": "019202e96d9f09dc0f325e7f7a2a",
            "Name": "live_test",
            "Whitelist": [
                "0.0.0.0"
            ],
            "OccupiedInputs": [
                "01937702c54509dc0f3269ca341f"
            ],
            "Region": "ap-shanghai"
        },
        "RequestId": "01941bb7827509dc0f320a9d3426"
    }
}
```

