**Example 1: 获取业务和攻击概览峰值**

获取业务和攻击概览峰值

Input: 

```
tccli waf DescribePeakValue --cli-unfold-argument  \
    --FromTime '2019-12-30 00:00:00' \
    --ToTime '2019-12-30 23:59:59' \
    --Domain abc.qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "Access": 0,
        "Up": 0,
        "Down": 0,
        "Attack": 0,
        "Cc": 0,
        "RequestId": "xxxx-xxxx-xxxxx"
    }
}
```

