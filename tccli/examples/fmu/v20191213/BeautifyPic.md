**Example 1: 调用成功示例**



Input: 

```
tccli fmu BeautifyPic --cli-unfold-argument  \
    --Url http://i2.sinaimg.cn/ty/nba/2015-07-05/U10236P6T12D7648505F44DT20150705114547.jpg\
    --Version 2019-12-13
```

Output: 
```
{
    "Response": {
        "ResultImage": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAFuAiYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqr...",
        "RequestId": "9cf173a5-4ae5-46fb-9898-6c876263770d"
    }
}
```

**Example 2: 调用失败示例**



Input: 

```
tccli fmu BeautifyPic --cli-unfold-argument  \
    --Url IamNotAUrl\
    --Version 2019-12-13
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.UrlIllegal",
            "Message": "URL格式不合法。"
        },
        "RequestId": "897d8a3d-6677-4c41-b647-f0a19a6dc13f"
    }
}
```

