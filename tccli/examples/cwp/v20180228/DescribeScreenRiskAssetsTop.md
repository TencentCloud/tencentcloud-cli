**Example 1: 大屏获取安全事件数统计数据**

大屏获取安全事件数统计数据


Input: 

```
tccli cwp DescribeScreenRiskAssetsTop --cli-unfold-argument  \
    --BusinessType 2
```

Output: 
```
{
    "Response": {
        "Chart": [
            {
                "Name": "1.1.1.1广州",
                "Value": 21
            }
        ],
        "RequestId": "f1d8e260-c75c-454d-bc84-34ce0ed8d9bf"
    }
}
```

