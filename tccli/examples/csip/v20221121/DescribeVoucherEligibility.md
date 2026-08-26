**Example 1: 正常请求**



Input: 

```
tccli csip DescribeVoucherEligibility --cli-unfold-argument  \
    --ActivityID 10001 \
    --ActID 20001
```

Output: 
```
{
    "Response": {
        "Available": 1,
        "RequestId": "e5b0c8f2-3a7d-4b1e-9c6f-2d8a4e5f7b3c"
    }
}
```

