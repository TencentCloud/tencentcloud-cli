**Example 1: uin是最高优先级特权用户，开通成功**

uin是最高优先级特权用户，并且相关特权开通成功

Input: 

```
tccli billing GrantDefaultPrivilege --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IsTopPriorityPrivilegeUin": true,
        "RequestId": "eced27f1-ff1c-4889-a195-f0354eb86e9d",
        "Status": "success"
    }
}
```

**Example 2: uin是最高优先级特权用户，开通失败，已提交重试**

uin是最高优先级特权用户，开通失败，已提交重试

Input: 

```
tccli billing GrantDefaultPrivilege --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IsTopPriorityPrivilegeUin": true,
        "RequestId": "c2892b58-15b0-40e7-bdea-05aa72551a2b",
        "Status": "retrying"
    }
}
```

**Example 3: uin是否是最高优先级特权用户状态未知，开通失败，已提交重试**

uin是否是最高优先级特权用户状态未知，开通失败，已提交重试

Input: 

```
tccli billing GrantDefaultPrivilege --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IsTopPriorityPrivilegeUin": null,
        "RequestId": "03e2b54f-7dfa-4b1b-b748-261757d80155",
        "Status": "retrying"
    }
}
```

