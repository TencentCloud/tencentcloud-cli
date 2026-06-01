**Example 1: 用户列表**



Input: 

```
tccli tchousex DescribeUserV2 --cli-unfold-argument  \
    --InstanceId instance-vzarb8go \
    --Limit 10 \
    --Offset 0 \
    --UserType 2 \
    --UserToken eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6IjdiYzRlMTMzLTdjMWEtNGUwMi1hZWI1LTY1MjY1ODgwMDkzMyIsImF1dGhvcml6ZWQiOnRydWUsImNlcnQiOiJ7XCJUbXBTZWNyZXRJZFwiOlwiQUtJRFRJRDAtWkV6blJDQnJTdm5yWmZ0eThweHBXVlNoUjh0WFktZVpldEhNMkxwWDZQc1J6dVljNkt4eEs4M0Q0MUVcIixcIlRtcFNlY3JldEtleVwiOlwiK1dPRDJhTjArc1UrTWo3dGdtWGxSbGh4UkZYendTaVhCMVB3N0hBQVU3Zz1cIixcIlRva2VuXCI6XCI2aHU5QVFpSkxxMzZwNjhIcUpLaXFmYzRNSU1qYTJtYTdjOTkzYjJmNmQwNmFjYTllOTc4ZGU2ODQ3ZmQxYzhlTVc3UEtjT2JxSkZPb1hGUWhxdTRYLXJMTDIyVk1FNWc3VjRVdjFFQXBoYmtFdWRhdS1tMTBhMFN5QUVBR3hBS2pjd3JaWHFjVl9FR1dhMUdEQjZQLVFaeDZSZk1PZm1BcWFZT3Z6dF9mYkxiNWM3dGIyNDh2d2s3bkdwdi1qU3YyaTZoLU9XOWNYbjRreWFnX24xb2x5cWxrcWJHWDdtWC1PQmpwaGxjVHExVGlGZlo1NDliSkFMUDY3N1l5Ml9tZFZUR3VRV3ZPNEZsNXM3M2hoR0N6Zl9RcUMwQmZNVVBYVk9sZzAtMlEyYlV2QXNIek5La2VQRG1ya0pOTE5Tb1BtcUJKSFN2aHVvUFBNNWgyV1RSX1NMRG8wSVkzNWhrSEdnWW96TWctX29yXzl6X1pJNXRzS2ZJUmhqdUFFeUQwOENSY0pQOUs4RlFfWE5BYklXWkFRXCJ9IiwiaW5zdGFuY2VfaWQiOiJpbnN0YW5jZS12emFyYjhnbyIsInVzZXJfbmFtZSI6IjEwMDAwNjgxMTgxOCJ9.g5XUJdatxnQtcfMFcJysuVEzBqJAeiADA8jOZ-diAHA
```

Output: 
```
{
    "Response": {
        "ErrorMsg": " ",
        "RequestId": "67bd9934-f2cb-43c8-b5ed-ef5c47a7dbdf",
        "ReturnData": "{\"TotalCount\":3,\"DescribeUserV2List\":[{\"UserName\":\"100006811818\",\"AssociatedUin\":\"100006811818\",\"AssociatedRole\":null,\"CreateTime\":\"2025-10-13T17:17:19+08:00\",\"Describe\":\"\",\"UserType\":2,\"PermissionMode\":1,\"AccountIdentity\":\"sysadmin\",\"PasswordUpdateTime\":\"2025-10-13T17:17:19+08:00\"},{\"UserName\":\"100043935658\",\"AssociatedUin\":\"100043935658\",\"AssociatedRole\":null,\"CreateTime\":\"2025-10-13T17:17:19+08:00\",\"Describe\":\"\",\"UserType\":2,\"PermissionMode\":1,\"AccountIdentity\":\"sysadmin\",\"PasswordUpdateTime\":\"2025-10-13T17:17:19+08:00\"},{\"UserName\":\"100044684253\",\"AssociatedUin\":\"100044684253\",\"AssociatedRole\":null,\"CreateTime\":\"2025-10-23T16:08:56+08:00\",\"Describe\":\"\",\"UserType\":2,\"PermissionMode\":1,\"AccountIdentity\":\"user\",\"PasswordUpdateTime\":\"2025-10-23T16:08:56+08:00\"}]}"
    }
}
```

