**Example 1: QueryPolicy**

披露策略Policy查看

Input: 

```
tccli tdid QueryPolicy --cli-unfold-argument  \
    --PolicyIndex 37
```

Output: 
```
{
    "Response": {
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425",
        "Id": 37,
        "PolicyId": 2000045,
        "CptId": 21414450,
        "PolicyData": "{\n  \"cptId\": 1,\n  \"gender\": 0,\n  \"tags\": 0,\n  \"userId\": 0,\n  \"userName\": 0\n}"
    }
}
```

