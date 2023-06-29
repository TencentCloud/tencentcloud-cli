**Example 1: 查询kms加密状态**

查询kms加密状态

Input: 

```
tccli tke DescribeEncryptionStatus --cli-unfold-argument  \
    --ClusterId cls-mu2or8b8
```

Output: 
```
{
    "Response": {
        "Status": "Opened",
        "ErrorMsg": " ",
        "RequestId": "73779803-e28b-481a-a350-eab5bada499b"
    }
}
```

