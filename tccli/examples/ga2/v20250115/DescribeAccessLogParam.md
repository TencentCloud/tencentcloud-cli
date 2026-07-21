**Example 1: 查看访问日志上报参数示例**



Input: 

```
tccli ga2 DescribeAccessLogParam --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "L4Param": [
            "session_time"
        ],
        "L7Param": [
            "request_method"
        ],
        "RequestId": "06f83c8f-9eff-478e-9c10-005d7d0b3776"
    }
}
```

