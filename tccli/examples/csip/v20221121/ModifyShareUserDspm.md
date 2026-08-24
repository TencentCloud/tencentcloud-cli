**Example 1: 修改dspm监测账号**



Input: 

```
tccli csip ModifyShareUserDspm --cli-unfold-argument  \
    --MemberId mem-68b8087a65261234 mem-ac092bdbb93c1234 mem-tencent-5090192288531234 mem-56c68ef19541234 mem-94eace433ec11234 mem-7c6daa49836d1234 \
    --SharedAppIDList 1308951234 1301841234 1256291234 1258641234
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "da0a28f2-c2d8-4f89-b4bc-f3928571f014",
        "Result": 0
    }
}
```

