**Example 1: 获取创建弹性单副本SSD硬盘的订单参数**



Input: 

```
tccli cbs SwitchParameterCreateRemoteDisks --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d"
    }
}
```

