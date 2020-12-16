**Example 1: DescribeAccountBalance正常请求**

正常请求的入参回参

Input: 

```
tccli iotvideo DescribeAccountBalance --cli-unfold-argument  \
    --AccountType 2
```

Output: 
```
{
    "Response": {
        "State": 0,
        "Balance": 7652,
        "LastUpdateTime": 1607069420,
        "AccountType": 2,
        "RequestId": "xx"
    }
}
```

**Example 2: DescribeAccountBalance异常请求**

请求异常的入参和出参

Input: 

```
tccli iotvideo DescribeAccountBalance --cli-unfold-argument  \
    --AccountType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "43348837-a756-4939-92b6-77c333c1b96e",
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "账号不存在"
        }
    }
}
```

