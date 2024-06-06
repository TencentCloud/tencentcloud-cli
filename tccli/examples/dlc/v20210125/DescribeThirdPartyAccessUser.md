**Example 1: 实例一**

查询注册的第三方访问用户信息

Input: 

```
tccli dlc DescribeThirdPartyAccessUser --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "584515f3-835f-459d-b93b-d6c6f64c0daa",
        "UserInfo": {
            "AppId": "123456",
            "CreateTime": "2024-05-22T09:49:56+08:00",
            "Id": 5,
            "Uin": "123456"
        }
    }
}
```

