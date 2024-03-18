**Example 1: 请求示例**

断开指定Sequence上行流

Input: 

```
tccli live DropLiveBackupStream --cli-unfold-argument  \
    --PushDomainName 5000.livepush.com \
    --AppName live \
    --StreamName test \
    --UpstreamSequence 2210463907505478124
```

Output: 
```
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

