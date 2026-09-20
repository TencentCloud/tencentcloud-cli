**Example 1: 创建 MANUAL 审批的 Registry**

响应体带 RequestId 与 RegistryId；后续获取详情用 DescribeRegistry。ApprovalMode 省略时默认 AUTO。

Input: 

```
tccli ags CreateRegistry --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

