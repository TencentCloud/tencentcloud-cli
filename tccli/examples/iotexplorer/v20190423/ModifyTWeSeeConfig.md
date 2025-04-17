**Example 1: 修改 TWeSee 配置**

修改 TWeSee 配置

Input: 

```
tccli iotexplorer ModifyTWeSeeConfig --cli-unfold-argument  \
    --ProductId MOU0U8SCZQ \
    --DeviceName new_131296974_1 \
    --EnableSummary False \
    --EnableSearch False \
    --Config {"type":"data"}
```

Output: 
```
{
    "Response": {
        "RequestId": "2dbdcb8c-d8cb-4f9d-a491-ff0dd3bb53b6"
    }
}
```

