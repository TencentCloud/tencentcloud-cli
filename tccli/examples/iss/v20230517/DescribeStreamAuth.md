**Example 1: 成功**

 

Input: 

```
tccli iss DescribeStreamAuth --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": 1300000000,
            "Id": "12345678-abcd-efgh-ijkl-1234567890abcd",
            "PullExpired": 10,
            "PullSecret": "123456",
            "PullState": 0,
            "PushExpired": 10,
            "PushSecret": "123456",
            "PushState": 0
        },
        "RequestId": "cf385ee3-30f4-4ee7-bfd4-a123f9a71380"
    }
}
```

