**Example 1: 示例1**



Input: 

```
tccli ioa DescribeDeliveryServer --cli-unfold-argument  \
    --ID 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Name": "dfa",
            "Description": "",
            "TargetKafkaAddress": "10.0.0.1",
            "TargetSyslogPort": 601,
            "TargetKafkaTopic": "t",
            "KafkaVersion": "2.2.2",
            "TargetHttpTimeout": 10,
            "KafkaSSLEnable": false,
            "KafkaSaslPassword": "gaeq0cK34imtGd+Lh+5EVr0FXY9YkZEjWdseJeacevMt5p8xZjQ5mnswhLezoDbf7PZWlHbOzcc8LILfY8SKBgSdF+4sG7Mh50xYPXzVnsTOh13nvAs0c7YdebDq7mutHTlIqLYNV/BMJ0Dm4t+3dM7yJ3ckFavnq8Uvoxx0eqKhhzQKmFX6hYVd+j0e5rz5Nmw1v0uAdMv6wJl+0uS8+QzfcBER7IEjP+5Dn7uQBL4NiD7seVO9U773XBqwOGruRsXTrsGbFZWn1IdkxY7elc12VXTZ91lON+gq+NeKbxrkLCwqJzDz6ztC9i6ehdIt2E60YwfoKWgrdW6nC36lDhsIS1CwUBHe43oSMiHHZIejaU7jDK6wz4mndjH1dF1m7p+aFm+kFqMfVjHprvmp+HcopqlFouf1hZuRP/EHw4j8kVw4L78RayXO3BPr4y6dGIWl2a6Hb1k81hMv3+EqwdJsDQvMlvN//kg07AIaTXQmMngOqRV9cA0zFdBet2TqglsjYDWTVaE6yOhYLM5kqyD/G0//Fz5LLWxKJ9cv9KFeKnlkRP0igd2Efoo9aSHUDCecBowNGYF5oXxkJh+yR/FU85YGMXPQQvO7KJgLoEI+kLW5A7XQrq2SiENL08RqOvezlWVoS8C6zJCKtSPxgfIYkgSwHy/zbZN/iYWOx/s=",
            "ID": 2395,
            "SSLSkipVerify": false,
            "TargetSyslogProtocol": "tcp",
            "Type": 2,
            "KafkaSaslUserName": "11"
        },
        "RequestId": "a6d47367-9be6-4212-a3bb-6179716cbbee"
    }
}
```

