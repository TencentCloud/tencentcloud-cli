**Example 1: 获取详情**



Input: 

```
tccli rum DescribeFOOMMallocProblemDetail --cli-unfold-argument  \
    --ProductId 0dc5283a55 \
    --ClientIdentify BC155210-0AAF-4889-8B59-03097BB1227E \
    --Feature AE2506C0E4BCDEE875D7880A5779C7BB \
    --RequestHeader BEGIN{"X-ProductId": "0dc5283a55","X-Tc-Username": "cdx_test"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"base_rsp\":{\"code\":0,\"msg\":\"success\"}",
        "Message": "",
        "RequestId": "aa97aeba-d8c5-40a1-b8f2-f6bd2cdf87f3"
    }
}
```

