**Example 1: 获取指定时间段内请求总数**

获取指定时间段内请求总数，这个接口不需要客户购买日志服务

Input: 

```
tccli waf DescribeAttackOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccessCount": 8550963579,
        "AttackCount": 63579,
        "ACLCount": 963579,
        "CCCount": 50963579,
        "BotCount": 963579,
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

