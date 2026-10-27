**Example 1: DescribeInstanceLoginMsg**



Input: 

```
tccli cvd DescribeInstanceLoginMsg --cli-unfold-argument  \
    --InstanceId cdi-a \
    --Force True \
    --DesktopName deskname \
    --UserId usera
```

Output: 
```
{
    "Response": {
        "RequestId": "rid",
        "LoginMsg": "gdsfhdskfJldsfadsFNBVB"
    }
}
```

