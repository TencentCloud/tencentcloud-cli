**Example 1: 查询是否注入风险服务配置**

查询是否注入风险服务配置

Input: 

```
tccli cwp DescribeInjectRiskyServiceSwitch --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "JavaShellInjectRiskyServiceStatus": 1,
        "TotalCount": 0,
        "RaspInjectRiskyServiceStatus": 0,
        "List": [],
        "RequestId": "8a9e1690-da5e-4086-9937-e3a5b53bcbcc"
    }
}
```

