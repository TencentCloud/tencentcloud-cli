**Example 1: 获取数字验证码成功示例**



Input: 

```
tccli faceid GetLiveCode --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "LiveCode": "4392",
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

**Example 2: 获取数字验证码失败示例**



Input: 

```
tccli faceid GetLiveCode --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation.Nonactivated",
            "Message": "未开通服务。"
        },
        "RequestId": "4a75418f-96f7-4045-955f-32a7dd1b08bf"
    }
}
```

