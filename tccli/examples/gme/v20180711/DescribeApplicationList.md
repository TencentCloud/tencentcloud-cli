**Example 1: 获取自己名下名称中含有“测试”字样的应用列表**

https://gme.tencentcloudapi.com/?Action=DescribeApplicationList
&ProjectId=0
&PageNo=0
&PageSize=10
&SearchText=测试
&<公共请求参数>

Input: 

```
tccli gme DescribeApplicationList --cli-unfold-argument  \
    --ProjectId 0 \
    --SearchText 测试 \
    --PageSize 10 \
    --PageNo 0
```

Output: 
```
{
    "Response": {
        "ApplicationList": [
            {
                "ServiceConf": {
                    "Porn": {
                        "Status": 1
                    },
                    "Live": {
                        "Status": 1
                    },
                    "RealTimeSpeech": {
                        "Status": 1
                    },
                    "RealTimeAsr": {
                        "Status": 1
                    },
                    "VoiceMessage": {
                        "Status": 1
                    }
                },
                "BizId": 1400000000,
                "AppType": 1,
                "AppName": "test",
                "ProjectId": 1,
                "AppStatus": 1,
                "CreateTime": 1
            }
        ],
        "Total": 1,
        "RequestId": "65ba570f-dbbb-4e3b-a412-5e285a2fecc9"
    }
}
```

