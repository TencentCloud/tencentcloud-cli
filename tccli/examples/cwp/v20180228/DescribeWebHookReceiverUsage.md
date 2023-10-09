**Example 1: 示例**

示例

Input: 

```
tccli cwp DescribeWebHookReceiverUsage --cli-unfold-argument  \
    --List.0.Id 28 \
    --List.0.Name 小小机器
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "PolicyName": "相同IM机器a，b",
                "ReceiverId": 28,
                "ReceiverName": "小小机器"
            },
            {
                "PolicyName": "相同IM机器a，b",
                "ReceiverId": 28,
                "ReceiverName": "小小机器"
            },
            {
                "PolicyName": "三七告警",
                "ReceiverId": 28,
                "ReceiverName": "小小机器"
            },
            {
                "PolicyName": "测试1",
                "ReceiverId": 28,
                "ReceiverName": "小小机器"
            }
        ],
        "RequestId": "ae5722b3-3c64-4c8c-b1ad-b8e13bdbfcc7",
        "TotalCount": 4
    }
}
```

