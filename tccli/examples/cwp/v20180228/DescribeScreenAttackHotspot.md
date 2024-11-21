**Example 1: 大屏获取安全事件数统计数据**

大屏获取安全事件数统计数据

Input: 

```
tccli cwp DescribeScreenAttackHotspot --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CreatedTime": "2022-06-28 19:27:26",
                "DstIp": "10.0.0.1",
                "EventName": "Atlassian Crowd和Atlassian Crowd Data Center 输入验证错误漏洞(CVE-2019-11580)",
                "Region": "ap-guangzhou",
                "SrcIp": "10.0.0.1"
            }
        ],
        "RequestId": "3dcfeooo-c2fa-4e5c-a1f7-9f28ce88f554"
    }
}
```

