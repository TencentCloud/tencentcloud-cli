**Example 1: 请求示例**



Input: 

```
tccli live DescribePullStreamConfigs --cli-unfold-argument  \
    --ConfigId 5674
```

Output: 
```
{
    "Response": {
        "PullStreamConfigs": [
            {
                "ConfigId": "5674",
                "FromUrl": "rtmp://3737.liveplay.myqcloud.com/txlive",
                "ToUrl": "rtmp://3954.livepush2.myqcloud.com/live/3954_462724865?&txSecret=xx",
                "AreaName": "深圳",
                "IspName": "电信",
                "StartTime": "2018-07-06T14:40:23Z",
                "EndTime": "2018-07-06T18:05:23Z",
                "Status": "2"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

