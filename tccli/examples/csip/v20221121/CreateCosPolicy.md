**Example 1: 添加cos告警策略**



Input: 

```
tccli csip CreateCosPolicy --cli-unfold-argument  \
    --CosPolicyInfo.PolicyName custom-bucket-read-policy \
    --CosPolicyInfo.PolicyType 1 \
    --CosPolicyInfo.PolicySource 2 \
    --CosPolicyInfo.PolicyAbnormalType 1 \
    --CosPolicyInfo.RiskLevel 1 \
    --CosPolicyInfo.PolicyContent e1wiVmVyc2lvblwiOlwiMi4wXCIsXCJTdGF0ZW1lbnRcIjpbe1wiRWZmZWN0XCI6XCJBbGxvd1wiLFwiUHJpbmNpcGFsXCI6e1wicWNzXCI6W1wicWNzOjpjYW06OnVpbi8xMDAwMTIzNDU2Nzg6dWluLzEwMDAxMjM0NTY3OFwiXX0sXCJBY3Rpb25cIjpbXCJjb3M6R2V0T2JqZWN0XCIsXCJjb3M6R2V0T2JqZWN0VmVyc2lvblwiXSxcIlJlc291cmNlXCI6W1wicWNzOjpjb3M6YXAtZ3Vhbmd6aG91OnVpZC8xMDAwMTIzNDU2Nzg6bXktYnVja2V0LypcIl19XX0= \
    --CosPolicyInfo.PolicyStatus 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

