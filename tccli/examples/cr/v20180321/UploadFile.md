**Example 1: 上传数据文件**

上传数据文件

Input: 

```
tccli cr UploadFile --cli-unfold-argument  \
    --Module Data \
    --Operation UploadFile \
    --FileUrl https%3A%2F%2Fcollection-robot-test-1254255210.cosgz.myqcloud.com%2F%25E8%25AF%2595%25E5%2590%25AC%25E6%25A8%25A1%25E6%259D%25BF.xls%3Fsign%3DvnIXGeAyqu4HwHkwLX5X0pic8sphPTEyNTQyNTUyMTAmaz1BS0lEMFR6T2NseXB6MDlaNGZwdVM1bzNRRmN6S2FyOXJJUGomZT0xNTI0ODI4NjMzJnQ9MTUyMjIzNjYzMyZyPTIyMzgxNzMwMSZmPS8lRTglQUYlOTUlRTUlOTAlQUMlRTYlQTglQTElRTYlOUQlQkYueGxzJmI9Y29sbGVjdGlvbi1yb2JvdC10ZJLH \
    --FileName %E8%AF%95%E5%90%AC%E6%A8%A1%E6%9D%BF.xls \
    --FileDate 2018-09-01
```

Output: 
```
{
    "Response": {
        "RequestId": "3b10df62-29a2-430b-8493-991b3f6846e8",
        "TaskId": 9
    }
}
```

