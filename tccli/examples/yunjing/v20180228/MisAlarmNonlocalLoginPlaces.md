**Example 1: 误报异地登录**

本接口{MisAlarmNonlocalLoginPlaces}将设置当前地点为常用登录地。

Input: 

```
tccli yunjing MisAlarmNonlocalLoginPlaces --cli-unfold-argument  \
    --Ids 1 2
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

