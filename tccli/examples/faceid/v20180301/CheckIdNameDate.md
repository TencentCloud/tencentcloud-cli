**Example 1: 身份信息及有效期核验成功示例**



Input: 

```
tccli faceid CheckIdNameDate --cli-unfold-argument  \
    --Name 韦小宝 \
    --IdCard ' 11204416541220243X' \
    --ValidityBegin 20160204 \
    --ValidityEnd 20260204
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "查询成功",
        "RequestId": "8695c53f-776f-4ff5-a66d-84e67b352d20"
    }
}
```

**Example 2: 身份信息及有效期核验不一致示例**



Input: 

```
tccli faceid CheckIdNameDate --cli-unfold-argument  \
    --Name 韦小宝 \
    --IdCard ' 11204416541220243X' \
    --ValidityBegin 20160204 \
    --ValidityEnd 20260204
```

Output: 
```
{
    "Response": {
        "Description": "不一致",
        "RequestId": "af4075de-427f-48a5-85cb-2be5b3751b76",
        "Result": "-1"
    }
}
```

