**Example 1: DescribeUnfixedDevices接口示例**



Input: 

```
tccli ioa DescribeUnfixedDevices --cli-unfold-argument  \
    --Kb 111 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Item": [
                {
                    "MacAddr": "abc",
                    "Name": "abc",
                    "GroupNamePath": "abc",
                    "Ip": "abc",
                    "Mid": "abc",
                    "GroupName": "abc",
                    "Id": 0
                }
            ],
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            }
        },
        "RequestId": "abc"
    }
}
```

**Example 2: DescribeUnfixedDevices**

DescribeUnfixedDevices

Input: 

```
tccli ioa DescribeUnfixedDevices --cli-unfold-argument  \
    --Kb 12334 \
    --Cond.PageSize 1 \
    --Cond.PageNum 1 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "f4cd6d8c-93bd-4a42-bb52-bcf6b0b8c63e"
    }
}
```

