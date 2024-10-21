**Example 1: 大屏获取安全事件数统计数据**

大屏获取安全事件数统计数据

Input: 

```
tccli cwp DescribeScreenEventsCnt --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Info": [
            {
                "Category": [
                    {
                        "Name": "入侵检测",
                        "Value": 41343
                    },
                    {
                        "Name": "网络攻击",
                        "Value": 5795
                    }
                ],
                "Title": "待处理风险总数",
                "Total": 47138
            }
        ],
        "RequestId": "42f1c2a0-088c-43bb-909f-b9d54809b1d1"
    }
}
```

