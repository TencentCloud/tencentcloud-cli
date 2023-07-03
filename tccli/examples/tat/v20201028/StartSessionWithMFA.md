**Example 1: 给实例abc开启会话**

给实例abc开启会话

Input: 

```
tccli tat StartSessionWithMFA --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "SessionId": "abc",
        "StreamUrl": "",
        "RequestId": "abc"
    }
}
```

