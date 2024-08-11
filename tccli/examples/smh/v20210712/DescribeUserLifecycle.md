**Example 1: 查询用户生命周期**



Input: 

```
tccli smh DescribeUserLifecycle --cli-unfold-argument  \
    --LibraryId smh08gcw6500e6jl \
    --Filter.Key PhoneNumber \
    --Filter.Value +86-13800000000
```

Output: 
```
{
    "Response": {
        "UserId": "user18llqxtbrcvgn",
        "IsolateTime": "2025-06-30T15:59:59Z",
        "DestroyTime": "2025-07-30T15:59:59Z",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

