**Example 1: 示例**

示例

Input: 

```
tccli cwp DescribeWebHookReceiver --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Addr": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=cbe03861-a7c6-48cf-a34c-44**",
                "Id": 9,
                "Name": "测试发送"
            },
            {
                "Addr": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d0c2fc25-23a2-4285-ab98-**",
                "Id": 17,
                "Name": "企微"
            }
        ],
        "RequestId": "a1fd9261-58a8-4947-877d-222198eeeb56",
        "TotalCount": 2
    }
}
```

