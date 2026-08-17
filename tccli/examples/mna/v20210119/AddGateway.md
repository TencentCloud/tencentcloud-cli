**Example 1: 添加网关**



Input: 

```
tccli mna AddGateway --cli-unfold-argument  \
    --ClusterId cluster-vpqultrhw6 \
    --Username jacky \
    --Password Qjlzjl**** \
    --GatewayIp 11.***.108.242 \
    --RegionId ap-chengdu
```

Output: 
```
{
    "Response": {
        "GatewayId": "mpgw-rp6tfdfpqp",
        "RegisterCenterUrl": "reg-rest-****.multipath.tencent-cloud.com:9300",
        "TelemetryUrl": "21.0.21.***:65002",
        "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdGFuZGFyZENsYWltcyI6eyJpYXQiOjE3ODUxNTY2MDEuNjE3MjM5LCJuYmYiOjE3ODUxNTY2MDEuNjE3MjR9LCJ******joibXBndy1ycDZ0ZmRmcHFwIiwibWdtdElwIjoiMTEuMTQxLjEwOC4yNDIifQ.etq0nOn1x0F59lXl3vBsiHx0b6HO0NtkQrd9Q6nZFbQ",
        "RequestId": "fac62d02-a63c-4c67-a528-3cca18ed44c6"
    }
}
```

