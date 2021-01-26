**Example 1: 删除异地登录记录**

本接口 (DeleteNonlocalLoginPlaces) 用于删除异地登录记录。

Input: 

```
tccli cwp DeleteNonlocalLoginPlaces --cli-unfold-argument  \
    --DelType Id \
    --Ids 123 456
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

