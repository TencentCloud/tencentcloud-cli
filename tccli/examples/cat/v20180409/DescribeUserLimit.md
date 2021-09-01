**Example 1: 获取用户可用资源限制 示例**



Input: 

```
tccli cat DescribeUserLimit --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MaxTaskNum": 10,
        "MaxAgentNum": 5,
        "MaxGroupNum": 5,
        "MinPeriod": 5,
        "RequestId": "88f4bf3d-7d7d-42b8-a7d3-5100436e2c46"
    }
}
```

