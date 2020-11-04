**Example 1: 查询配置**



Input: 

```
tccli tsf DescribeConfig --cli-unfold-argument  \
    --ConfigId dcfg-qabr26yl
```

Output: 
```
{
    "Response": {
        "RequestId": "2e68ea83-3799-4fb0-ba9b-ab8be2488d98",
        "Result": {
            "ConfigId": "dcfg-qabr26yl",
            "ConfigName": "test_pay_center",
            "ConfigVersion": "0.0.9",
            "ConfigVersionDesc": "默认100元",
            "ConfigValue": "facade:\r\n  white-list:\r\n       - 10.3.1.34\r\n       - 10.3.1.32\r\n       - 212.64.13.188\r\n       - 172.16.0.192\r\norder:\r\n  amount:\r\n    min: 1\r\n    wxScoreMin: 1\r\n    wxScoreMax: 20000 \r\n    enterpriseAmount: 10000 \r\n    refundAmountMax: 1000000             ",
            "CreationTime": "2019-05-28 20:23:35",
            "LastUpdateTime": null,
            "ConfigVersionCount": null,
            "ApplicationId": "application-6ym9pbag",
            "ApplicationName": "test_pay_center",
            "DeleteFlag": false,
            "ConfigType": null
        }
    }
}
```

