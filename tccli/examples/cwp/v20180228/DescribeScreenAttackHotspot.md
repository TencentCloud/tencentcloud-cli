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
                "EventName": "xx",
                "SrcIp": "xx",
                "Region": "xx",
                "DstIp": "xx",
                "CreatedTime": "xx"
            }
        ],
        "RequestId": "0e078e5e-32bf-41ba-853c-88c697888d99"
    }
}
```

