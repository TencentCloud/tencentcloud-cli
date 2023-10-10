**Example 1: 获取漏洞紧急通知信息**

获取漏洞紧急通知信息

Input: 

```
tccli cwp DescribeVulEmergentMsg --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "EmergentMsgList": [
            {
                "VulId": 100488,
                "PublishTime": "2020-03-13 00:00:00",
                "Name": "Windows SMB远程代码执行漏洞"
            }
        ]
    }
}
```

