**Example 1: 创建文件凭证**



Input: 

```
tccli bsca CreateFileTicket --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TicketId": "1234567890-815e8385-82f8-4f8a-b35f-a7e5eac218c2",
        "URL": "https://bsca-1234567890.cos.ap-guangzhou.myqcloud.com/upload/1234567890-815e8385-82f8-4f8a-b35f-a7e5eac218c2",
        "RequestHeaderSet": [
            {
                "Key": "Authorization",
                "Value": "q-sign-algorithm=sha1&q-ak=SecretID&q-sign-time=1631016205;1631019805&q-key-time=1631016205;1631019805&q-header-list=host&q-url-param-list=&q-signature=signature"
            }
        ],
        "RequestId": "eacfb401-a322-493a-8e36-83b295412345"
    }
}
```

