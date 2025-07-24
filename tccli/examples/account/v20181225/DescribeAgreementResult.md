**Example 1: 查询用户选择结果**

查询用户选择结果示例

Input: 

```
tccli account DescribeAgreementResult --cli-unfold-argument  \
    --Scenario cvm_buy \
    --FollowOption 0
```

Output: 
```
{
    "Response": {
        "OpUin": "800000324591",
        "Option": "1",
        "RequestId": "124b60ae-1272-4ed1-8369-165737487265",
        "Result": "Agree"
    }
}
```

