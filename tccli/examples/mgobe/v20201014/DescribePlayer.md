**Example 1: 查询玩家信息**

查询玩家信息

Input: 

```
tccli mgobe DescribePlayer --cli-unfold-argument  \
    --GameId obg-fr4vwil4 \
    --PlayerId joe123455
```

Output: 
```
{
    "Response": {
        "Player": {
            "OpenId": "joe123455",
            "Name": "xx",
            "CustomProfile": "worker",
            "IsRobot": false,
            "PlayerId": "joe123455",
            "CustomPlayerStatus": 1,
            "TeamId": "xx"
        },
        "RequestId": "xx"
    }
}
```

