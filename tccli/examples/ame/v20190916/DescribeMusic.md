**Example 1: 获取曲库包歌曲播放信息-正常示例**



Input: 

```
tccli ame DescribeMusic --cli-unfold-argument  \
    --ItemId xxxx \
    --IdentityId xx \
    --SubItemType MP3-64K-FTD-P
```

Output: 
```
{
    "Response": {
        "Music": {
            "AuditionBegin": 0,
            "AuditionEnd": 0,
            "FileExtension": "mp3",
            "FileSize": 3475953,
            "Url": "/content/09/800/9860965-MP3-64K-FTD.mp3?sign=71a19ae9f06313071f5876fbc4fc5c30&t=5d81f154&transDeliveryCode=YQUFAR@0@1568791612@S@3e760189cf194262",
            "FullUrl": "http://xxx.com/content/09/800/9860965-MP3-64K-FTD.mp3?sign=71a19ae9f06313071f5876fbc4fc5c30&t=5d81f154&transDeliveryCode=YQUFAR@0@1568791612@S@3e760189cf194262"
        },
        "RequestId": "s1568791637852491000"
    }
}
```

**Example 2: 获取曲库包歌曲播放信息-版权方错误示例**

在Error为ResourceNotFound时，Message中包含Code信息为版权方的错误码，具体含义如下：
101 无结果
102 内容无权限获取
103 内容因版权原因下架
104 内容仅支持下载，不可在线播放
105 内容需要付费获取
106 部分资源内容状态不同
1001 输入参数错误
1004 第三方API错误
1005 支付错误
1006 非支持支付模式
1007 系统错误
1008 其他系统错误
1009 Token过期
1205 用户账户不存在
5023 超过当日下载最大量
5024 超过当月下载最大量
5000-5999 其他功能错误定义

Input: 

```
tccli ame DescribeMusic --cli-unfold-argument  \
    --ItemId xxxx \
    --IdentityId xx \
    --SubItemType MP3-64K-FTD-P
```

Output: 
```
{
    "Response": {
        "RequestId": "s1575025791424544000"
    }
}
```

