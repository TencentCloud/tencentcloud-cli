**Example 1: 新建用户**



Input: 

```
tccli dasb CreateUser --cli-unfold-argument  \
    --UserName xx \
    --ValidateTo 2020-09-22T00:00:00+00:00 \
    --RealName xx \
    --GroupIdSet 1 1 1 \
    --Phone xx \
    --ValidateFrom 2020-09-22T00:00:00+00:00 \
    --Email xx \
    --AuthType 1
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "xx"
    }
}
```

