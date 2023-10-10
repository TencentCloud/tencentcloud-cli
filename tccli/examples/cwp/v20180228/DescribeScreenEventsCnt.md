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
                        "Name": "xx",
                        "Value": 1
                    }
                ],
                "Total": "xx",
                "Title": "xx"
            }
        ],
        "RequestId": "0e078e5e-32bf-41ba-853c-88c697888d99"
    }
}
```

