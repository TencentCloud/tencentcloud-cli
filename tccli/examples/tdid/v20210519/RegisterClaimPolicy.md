**Example 1: RegisterClaimPolicy**

披露策略Policy注册

Input: 

```
tccli tdid RegisterClaimPolicy --cli-unfold-argument  \
    --CptIndex 48 \
    --Policy {
  "cptId": 1,
  "gender": 0,
  "age": 1,
  "userId": 0,
  "userName": 0
}
```

Output: 
```
{
    "Response": {
        "Id": 39,
        "PolicyId": 2000047,
        "RequestId": "xx"
    }
}
```

