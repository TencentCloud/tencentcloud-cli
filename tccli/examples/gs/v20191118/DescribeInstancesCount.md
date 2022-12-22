**Example 1: 获取实例总数和运行数**

查询手游运行数

Input: 

```
tccli gs DescribeInstancesCount --cli-unfold-argument  \
    --GameId game-zasfwedr \
    --GameType MOBILE
```

Output: 
```
{
    "Response": {
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022",
        "Total": 590,
        "Running": 480
    }
}
```

