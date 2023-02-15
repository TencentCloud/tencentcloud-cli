**Example 1: CreateSession示例**

CreateSession示例

Input: 

```
tccli car CreateSession --cli-unfold-argument  \
    --UserIp 125.127.178.228 \
    --ClientSession eyJhYmMiOjEyM30= \
    --UserId cg_user
```

Output: 
```
{
    "Response": {
        "ServerSession": "eyJ4dHoiOjc4OX0=",
        "RequestId": "fcf4146f-64d3-496c-88dc-d12f832de313"
    }
}
```

