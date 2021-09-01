**Example 1: 调用失败示例**



Input: 

```
tccli bda DeletePerson --cli-unfold-argument  \
    --PersonId 123131231
```

Output: 
```
{
    "Response": {
        "RequestId": "27304486-69f3-47fd-b8ce-b7436ec8486b"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda DeletePerson --cli-unfold-argument  \
    --PersonId testG10P1
```

Output: 
```
{
    "Response": {
        "RequestId": "10f9a902-184e-40d6-b09d-e85f0c2dcfba"
    }
}
```

