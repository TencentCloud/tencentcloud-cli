**Example 1: 修改账号主机**

修改账号主机

Input: 

```
tccli cynosdb ModifyAccountHost --cli-unfold-argument  \
    --ClusterId cynosdbmysql-on5xw0ni \
    --NewHost 192.168.12.15 \
    --Account.AccountName tomo1 \
    --Account.Host %
```

Output: 
```
{
    "Response": {
        "RequestId": "3558f586-4f83-4f3b-aabc-49d20126f657"
    }
}
```

