**Example 1: 验证芯片烧录信息**

第三次认证成功，剩余7次验证次数。

Input: 

```
tccli iottid VerifyChipBurnInfo --cli-unfold-argument  \
    --Data AZAAEAAAXS6R1BkGt8oo4rkDePv8168JJOMMG3yqIxfBEgAAtNBk5qWRh7x9CIIaA+KBhMoKsw6qIQp0+poRIucWz3nwKzEPLs2jlZvJlUbbvjmnoxMoCQ6dXamqOUuh2E3QQGUyMQFobtbW8Fu0za9BpiaUTPCiTZWB6jLVPlFDcwU9
```

Output: 
```
{
    "Response": {
        "LeftTimes": 7,
        "Pass": true,
        "RequestId": "b410542c-b7b1-439f-99b7-6767cbf41f59",
        "VerifiedTimes": 3
    }
}
```

**Example 2: 验证芯片烧录信息失败**

TID[001000005d3eabdb5e14103e8b542d21]非烧录完成状态（未烧录或已在使用控制台被空发/激活）

Input: 

```
tccli iottid VerifyChipBurnInfo --cli-unfold-argument  \
    --Data AZAAEAAAXS6R1BkGt8oo4rkDePv8168JJOMMG3yqIxfBEgAAtNBk5qWRh7x9CIIaA+KBhMoKsw6qIQp0+poRIucWz3nwKzEPLs2jlZvJlUbbvjmnoxMoCQ6dXamqOUuh2E3QQGUyMQFobtbW8Fu0za9BpiaUTPCiTZWB6jLVPlFDcwU9
```

Output: 
```
{
    "Response": {
        "RequestId": "fb65e97b-8913-4259-82a3-7a618a3abda5"
    }
}
```

