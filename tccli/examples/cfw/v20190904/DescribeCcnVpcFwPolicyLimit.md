**Example 1: VPC防火墙策略限制**



Input: 

```
tccli cfw DescribeCcnVpcFwPolicyLimit --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CcnPolicyCidrLenLimit": 100,
        "CcnPolicyGroupLenLimit": 50,
        "CcnPolicyInterconnectPairLenLimit": 10,
        "RequestId": "f6d6864d-76d5-4adc-87ae-2eab50058b48"
    }
}
```

