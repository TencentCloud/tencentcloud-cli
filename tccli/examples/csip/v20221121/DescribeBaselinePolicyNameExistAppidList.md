**Example 1: 获取策略名字所属的用户列表**

获取策略名字所属的用户列表

Input: 

```
tccli csip DescribeBaselinePolicyNameExistAppidList --cli-unfold-argument  \
    --PolicyName ad \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "AppidList": [
            200000000
        ],
        "RequestId": "a6acf02d-ac9f-4937-95ea-990420af946e"
    }
}
```

