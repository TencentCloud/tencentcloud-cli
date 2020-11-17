**Example 1: CreateMmsInstance**



Input: 

```
tccli zj CreateMmsInstance --cli-unfold-argument  \
    --License KA3431QZPU \
    --InstanceName aaa \
    --Title bbb \
    --Sign 腾讯科技 \
    --Contents.0.ContentType 1 \
    --Contents.0.Content abcdefg \
    --Contents.1.ContentType 2 \
    --Contents.1.Content https://zhuji-public-beta-1256886009.cos.ap-shanghai.myqcloud.com/za/202002/dc293ac5260adc2d84637c1ad993feed.jpg
```

Output: 
```
{
    "Response": {
        "Data": {
            "ReturnCode": 0,
            "ReturnMsg": "",
            "InstanceId": 1140
        },
        "RequestId": "111111"
    }
}
```

