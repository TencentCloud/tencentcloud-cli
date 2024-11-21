**Example 1: 运行时高危系统调用系统名称列表**



Input: 

```
tccli tcss DescribeRiskSyscallNames --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SyscallNames": [
            "chroot"
        ],
        "TotalCount": 1,
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

