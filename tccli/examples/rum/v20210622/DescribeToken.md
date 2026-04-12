**Example 1: 生成token**



Input: 

```
tccli rum DescribeToken --cli-unfold-argument  \
    --RequestHeader BEGIN{"X-ProductId": "0dc5283a55","X-Tc-Username": "cdx_test"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"code\":0,\"base_rsp\":{\"code\":0,\"msg\":\"success\"},\"token\":\"8b2ba517a84a2e6f740bb5b168e03d9e\",\"isTrpc\":true,\"traceId\":\"b17677bb8b941677c9170226367e7ab9\",\"timestamp\":\"2025-05-23 14:56:51.395\"}",
        "Message": "",
        "RequestId": "9b6fe086-a1d0-4a10-9171-af72e4f4a254"
    }
}
```

