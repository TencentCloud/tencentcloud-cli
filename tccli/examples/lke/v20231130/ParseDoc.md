**Example 1: 文档解析**

文档解析

Input: 

```
tccli lke ParseDoc --cli-unfold-argument  \
    --Name 微信城市服务CityID说明文档.docx \
    --Url https://wximg.qq.com/cityservices/doc/res/cityservices_cityids.docx \
    --TaskId D78iBBGi \
    --Policy default \
    --Operate split
```

Output: 
```
{
    "Response": {
        "RequestId": "8ea5a507-108f-4b05-add4-b07de8580590",
        "TaskId": "D78iBBGi"
    }
}
```

