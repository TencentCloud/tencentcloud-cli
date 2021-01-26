**Example 1: 查询房间信息**

查询房间信息

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

