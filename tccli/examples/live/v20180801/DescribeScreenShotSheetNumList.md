**Example 1: 请求示例**

查询直播增值业务--截图的张数。

Input: 

```
tccli live DescribeScreenShotSheetNumList --cli-unfold-argument  \
    --StartTime 2019-11-07T16:00:00Z \
    --EndTime 2019-11-09T15:59:00Z
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Num": 39623970,
                "Time": "2019-11-07T16:00:00Z"
            },
            {
                "Num": 41876427,
                "Time": "2019-11-08T16:00:00Z"
            }
        ],
        "RequestId": "k54e3deb-f318-4147-8a68-3c959642f9ec"
    }
}
```

