**Example 1: 大屏获取安全事件数统计数据**

大屏获取安全事件数统计数据

Input: 

```
tccli cwp DescribeScreenRiskAssetsTop --cli-unfold-argument  \
    --BusinessType 1
```

Output: 
```
{
    "Response": {
        "Chart": [
            {
                "Name": "xx",
                "Value": 1
            }
        ],
        "RequestId": "0e078e5e-32bf-41ba-853c-88c697888d99"
    }
}
```

