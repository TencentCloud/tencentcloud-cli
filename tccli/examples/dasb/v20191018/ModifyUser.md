**Example 1: 修改用户信息**

修改用户信息

Input: 

```
tccli dasb ModifyUser --cli-unfold-argument  \
    --Id 1 \
    --ValidateTo 2020-09-22T00:00:00+00:00 \
    --RealName xx \
    --GroupIdSet 1 1 1 \
    --Phone xx \
    --ValidateFrom 2020-09-22T00:00:00+00:00 \
    --Email xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

