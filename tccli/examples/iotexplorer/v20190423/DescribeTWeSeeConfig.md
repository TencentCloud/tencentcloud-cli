**Example 1: 查询 TWeSee 配置**

查询 TWeSee 配置

Input: 

```
tccli iotexplorer DescribeTWeSeeConfig --cli-unfold-argument  \
    --ProductId MOU0U8SCZQ \
    --DeviceName new_131296974_1
```

Output: 
```
{
    "Response": {
        "Config": "{\"type\":\"data\"}",
        "EnableSearch": false,
        "EnableSummary": false,
        "RequestId": "b96234ba-edc7-491d-a1c7-b12081a50a3c"
    }
}
```

